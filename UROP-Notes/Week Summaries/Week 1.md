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

- LSODA
- RK45

Since the focus is not on the numerical solutions, as they are expected to be many orders of magnitude more accurate and perform similarly for non-stiff problems, the standard LSODA algorithm is used in the first instance.

```jupyter
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 1)
y = np.exp(-x) * np.sin(4 * np.pi * x)
plt.plot(x,y)
pass
```