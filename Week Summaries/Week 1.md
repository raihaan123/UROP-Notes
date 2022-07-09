# Week 1
#summary 


#### Contents
- Kickoff meeting with Davide ([[Week 1#^Kickoff]])
- Setting [[Research Objectives]]
- Solving the [[Van der Pol Oscillator]]using numerical solvers!


## Outline
Welcome to week 1 of the UROP research project! 

Meeting with Davide on Wednesday 6th of July, we discussed the structure and running of the project, its main deliverables and prospective timelines. Usmaan, another UROP student, was also present in the meeting. [[Research Objectives]] were mutually agreed on and are updated on the CARG Sharepoint. ^Kickoff

Before even considering Physics Informed Machine Learning, it is important to set a benchmark.

```jupyter
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 1)
y = np.exp(-x) * np.sin(4 * np.pi * x)
plt.plot(x,y)
pass
```