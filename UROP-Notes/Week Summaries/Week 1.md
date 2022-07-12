# Week 1
#summary 


#### Contents
- Kickoff meeting with Dr Amato ([[Week 1#^Kickoff]])
- Setting [[Research Objectives]]
- Solving the [[Van der Pol Oscillator]] using numerical solvers!


## Outline
Welcome to week 1 of the UROP research project! 

Meeting with Davide on Wednesday 6th of July, we discussed the structure and running of the project, its main deliverables and prospective timelines. Usmaan, my fellow UROP student ~~and my so-called nephew~~, was also present in the meeting. [[Research Objectives]] were mutually agreed on and will be kept up-to-date here and on the CARG Sharepoint. ^Kickoff

Before even considering Physics Informed Machine Learning, it is important to set a benchmark. A model ODE - the [[Van der Pol Oscillator]] - and numerical solver needed to be selected first. Below are listed several commonly used time-marching algorithms.

- Euler methods
- RK45
- LSODA
- (Look into others)

Since the focus is not on the numerical solutions, as they are expected to be many orders of magnitude more accurate and perform similarly for non-stiff problems, the standard LSODA algorithm implemented in SciPy's `scipy.integrate.odeint` method is used in the first instance.

## Numerical Solution
The following is my Python implementation of a numerical solver for the [[Van der Pol Oscillator]] calculated using LSODA, a very robust ODE integrator. 
>The block below is formatted with Obsidian's Jupyter extension and will run just as fast - to run this natively, go to the extension settings and add the path to your chosen Python 3 environment, install the dependencies and hit run!
>
>(Try changing $\mu$!)

```jupyter
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Damping coefficient mu
mu = 1

# Function for VdP oscillator
X_dot = lambda X, t: np.array([X[1], mu*(1-X[0]**2)*X[1]-X[0]]) 

# Generating solution mesh
lim = 3
n_phasors = 30
  
ax1 = np.linspace(-lim, lim, n_phasors)
ax2 = np.linspace(-lim, lim, n_phasors)
AX1, AX2 = np.meshgrid(ax1, ax2)

# Creating figure with matplotlib
fig = plt.figure(figsize=(10,10), dpi=300)
fig.patch.set_facecolor('white')

plt.title(f"Van der Pol oscillator - Phase Portrait for $\mu$ = {mu}", fontsize=20)
plt.xlabel('$x_1$', fontsize=15)
plt.ylabel('$x_2$', fontsize=15)
plt.xlim([-lim, lim])
plt.ylim([-lim, lim])
  

'''
Phase portrait of the VdP oscillator
'''

# These hold the solutions
x1 = X_dot([AX1, AX2], 0)[0]
x2 = X_dot([AX1, AX2], 0)[1]

plt.quiver(AX1, AX2, x1, x2, color='r')


'''
Particular solution for the VdP oscillator for some initial conditions
'''

# Time vector
t = np.linspace(0, 100, 3000)

# List of matplotlib colors
col = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

# Family of initial conditions
for i, X0_1 in enumerate([0, 0.5, 1, 1.5, 2, 2.5, 3]):

	# Initial conditions
	X0 = np.array([X0_1, 0])
	
	# Solving ODE system using LSODA
	x = odeint(X_dot, X0, t)
	
	plt.plot(x[:,0], x[:,1], '-', color=col[i], linewidth=2)
	plt.plot([x[0,0]], [x[0,1]], 'o', color=col[i])
	plt.plot([x[-1,0]], [x[-1,1]], 's', color=col[i])

plt.show()
```

## Initial Thoughts on [[PINNs]]
There are -many- different implementation of [[PINNs]] across literature but they all share the fundamental idea of a data-driven approach to solving differential equations. 