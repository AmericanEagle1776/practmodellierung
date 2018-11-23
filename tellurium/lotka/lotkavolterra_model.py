# Import packages
import tellurium as te
import matplotlib.pyplot as plt
import numpy as np
plt.switch_backend('TkAgg')
#%matplotlib inline

lotka_volterra = """
# Compartments
compartment farm = 100 litre;
compartment woods = 100 litre;

# Reactions
r1 in farm: sheep -> 2sheep; k1 * sheep;
r2: sheep + wolf -> 2wolf; k2 * sheep * wolf;
r3: wolf -> ; k3 * wolf;

# Species (and Initial values)
sheep = 200;
wolf = 50;

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
rr.integrator='gillespie'
result = rr.simulate(0, 100, selections=['time', 'sheep', 'wolf'])

# Plot and annotate the results (include axis descriptions)

rr.plot(ytitle='number',xtitle='time')

plt.show()

sbml_model = te.antimonyToSBML(lotka_volterra)
with open('lotka_volterra.xml','w') as f:
    f.write(sbml_model)
# For the fast coders: Include here a parameter scan


# Comment: Later you can do this in a better and prettier way in matplotlib (Lecture on Friday)