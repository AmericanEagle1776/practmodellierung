# Import packages
import tellurium as te
import matplotlib.pyplot as plt
import numpy as np
plt.switch_backend('TkAgg')
#%matplotlib inline

lotka_volterra = """
# Reactions or ODEs
r1: x -> 2x; k1 * x;
r2: x + y -> 2y; k2 * x *y;
r3: y -> ; k3 * y;

# Species (and Initial values)
x = 20;
y = 5;

# Units
unit ps = 1/second;

# Parameters
k1 = 0.1 ps;
k2 = 0.01 ps;
k3 = 0.2 ps;
"""

# Load the model
rr = te.loada(lotka_volterra)

# Simulate it (here you choose what to plot)
result = rr.simulate(0, 100, selections=['time', 'x', 'y'])

# Plot and annotate the results (include axis descriptions)

rr.plot(ytitle='numbero',xtitle='time in s')

plt.savefig('lotkaplot.pdf')

sbml_model = te.antimonyToSBML(lotka_volterra)
with open('lotka_volterra.xml','w') as f:
    f.write(sbml_model)

# For the fast coders: Include here a parameter scan


# Comment: Later you can do this in a better and prettier way in matplotlib (Lecture on Friday)