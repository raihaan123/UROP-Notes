import  deepxde as dde
from    deepxde.backend import tf
import  numpy as np
import  matplotlib.pyplot as plt
from    scipy.integrate import odeint
import  wandb

sweep_config = {
    "name" : "optimisation-sweep",
    # "method": "random",
    
    # Bayesian optimization of the parameters
    "method": "bayes",
    "metric": {"name": "val_loss", "goal": "minimize"},

    "parameters" : {
    
        "depth"       : {"values" : np.arange(1, 31).tolist()},
        "height"      : {"values" : np.arange(1, 101).tolist()},
        "num_domain"  : {"values" : np.arange(1000, 3000, 100).tolist()}    
  }
}

sweep_id = wandb.sweep(sweep_config, project="PINNs", entity="raihaan123")


# PDE parameters
mu = 2
X0 = [1, 0]
t_f = 20

# Hyperparameters for the ADAM optimiser
# alpha           = 0.005
# loss_weights    = [3, 0.1, 0.1]    # [X, x1(0), x2(0)] errors

# VdP oscillator
ODE         = lambda X, t:  np.array([X[1], mu*(1-X[0]**2)*X[1]-X[0]])
true_sol    = lambda t:     odeint(ODE, X0, t)

# The PDE problem
def VdP(t, y):
    dy_dt = dde.grad.jacobian(y, t)
    d2y_dt2 = dde.grad.hessian(y, t)
    return  d2y_dt2 - mu * (1 - y ** 2) * dy_dt + y

# Time domain definition
geom = dde.geometry.TimeDomain(0, t_f)

# Boundary domain function - for time domain
def boundary_l(t, on_initial):
    return on_initial and np.isclose(t[0], 0)

# x1(0) = 0.5
bc_func1 = lambda inputs, outputs, X: outputs - X0[0]

# x2(0) = 0
bc_func2 = lambda inputs, outputs, X: dde.grad.jacobian(outputs, inputs, i=0, j=None) - X0[1]

# Defining as ICs
ic1 = dde.icbc.OperatorBC(geom, bc_func1, boundary_l)
ic2 = dde.icbc.OperatorBC(geom, bc_func2, boundary_l)

def train():
    with wandb.init() as run:
        config = wandb.config

        # Define the PDE problem
        data = dde.data.TimePDE(geom, VdP, [ic1, ic2], config["num_domain"], 2, num_test=50000)

        # Solver architecture
        layer_size = [1] + [config["height"]] * config["depth"] + [1]
        # layer_size = [1] + [10]*2 + [2]*2 + [10]*2 + [1]          # Fun experiment! Does there exist a linear coordinate frame for the ODE?
        activation = "tanh"
        initializer = "Glorot uniform"
        net = dde.nn.FNN(layer_size, activation, initializer)

        def input_transform(t):
            return tf.concat(
                (
                    t,
                    # t%1,
                    # tf.log_sigmoid(t),
                    tf.cos(t),
                    tf.sin(t)
                    # tf.sin(2 * t),
                    # tf.sin(3 * t),
                    # tf.sin(4 * t)
                ),
                axis=1,
            )

        net.apply_feature_transform(input_transform)


        # Create a Model using the PDE and neural network definitions
        model = dde.Model(data, net)

        # Compile the model!
        model.compile("L-BFGS")
        loss_history, train_state = model.train()
        
        loss_test = train_state.loss_test[0]
        wandb.log({"val_loss": loss_test})

# model.compile(
#     "adam", lr=alpha, loss_weights=loss_weights     # Removed metrics=["l2 relative error"]
# )

# losshistory, train_state = model.train(iterations=20000)
# dde.saveplot(losshistory, train_state, issave=True, isplot=True)

count = 100 # number of runs to execute
wandb.agent(sweep_id, function=train, count=count)