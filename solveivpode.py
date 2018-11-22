#implementing a ODES (lotka volterra) including plotting

from scipy.integrate import solve_ivp
import numpy as numpy
import matplotlib.pyplot as plt

# parameters
a = 1.5
b = 1
c = 3
d = 1

#timegrid 
time = (0, 10)

# initial values
rabs0 = 50
foxes0 = 100
y0 = [rabs0, foxes0]

#function
def f(t, y):
    rabsi = y[0]
    foxesi = y[1]
    rabs1 = a*rabsi - b*rabsi*foxesi
    foxes1 = c*rabsi*foxesi - d*foxesi
    return [rabs1, foxes1]

result = solve_ivp(f, time, y0, method='LSODA')

fig1 = plt.figure()
sub1 = fig1.add_subplot(111)
sub1.plot(result.t, result.y[0], label='rabbers' )
sub1.plot(result.t, result.y[1], label='foxes')
sub1.set_xlabel('time in days')
sub1.set_ylabel('pop size in absolute numbers')
fig1.legend(fontsize='small')
plt.show()
