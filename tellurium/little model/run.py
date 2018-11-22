import tellurium as te
import matplotlib.pyplot as plt
plt.switch_backend('TkAGg')
# load

#rr = te.loada('simple_model.txt')
rr = te.loada('simple_model_ode.txt')

#sim
result = rr.simulate(0, 100)

#plot
rr.plot(result)
#plt.savefig('lol.pdf')
plt.show()