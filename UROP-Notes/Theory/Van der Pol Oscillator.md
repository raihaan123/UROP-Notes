# Van der Pol Oscillator
#theory

Wikipedia is a great place to start-
> In [dynamics](https://en.wikipedia.org/wiki/Dynamical_system "Dynamical system"), the **Van der Pol oscillator** is a [non-conservative](https://en.wikipedia.org/wiki/Conservative_force "Conservative force") [oscillator](https://en.wikipedia.org/wiki/Oscillator "Oscillator") with [non-linear](https://en.wikipedia.org/wiki/Nonlinearity "Nonlinearity") [damping](https://en.wikipedia.org/wiki/Damping_ratio "Damping ratio"). It evolves in time according to the second-order [differential equation](https://en.wikipedia.org/wiki/Differential_equation):
> # $\frac{d^{2} x}{d t^{2}}-\mu\left(1-x^{2}\right) \frac{d x}{d t}+x=0$
> where _x_ is the position [coordinate](https://en.wikipedia.org/wiki/Coordinate_system "Coordinate system")—which is a [function](https://en.wikipedia.org/wiki/Function_(mathematics) "Function (mathematics)") of the time _t_, and _μ_ is a [scalar](https://en.wikipedia.org/wiki/Scalar_(mathematics) "Scalar (mathematics)") parameter indicating the nonlinearity and the strength of the damping.

So its a non-linear 2nd-order ODE - pretty common! In the case where the damping coefficient $\mu$ is 0, it is further simplified into a linear form that resembles a simple harmonic oscillator and is fully conservative.

To form the standard non-linear representation, $X'(t) = f(t,X)$, we can define the state vector $X = [x, x']$:

### $\dot{X}=\left[\begin{array}{c}X_1 \\ \mu\left(1-X_0^{2}\right) X_1-X_0\end{array}\right]$

This form of the equation is used in the time marching algorithm in the `numerical_solution.ipynb` in the IPython Notebooks directory.

```jupyter
X_dot = lambda X, mu, t: np.array([X[1], mu*(1-X[0]**2)*X[1]-X[0]])
```

![Van der Pol - Phase Portrait](phase-portrait.png)