import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
import odesyslotkavolterra as o

end = 100
result = spi.solve_ivp(o.f, (0, end), o.y0, t_eval=np.linspace(0, end, 10000))
sheep = result.y[0]
wolves = result.y[1]

fig1 = plt.figure()
sub1 = fig1.add_subplot(311)
sub1.plot(result.t, sheep, label='sheeps')
sub1.plot(result.t, wolves, label='wolves', ls='--')
sub1.legend()
sub2 = fig1.add_subplot(312)
sub2.plot(sheep[0:5000], wolves[0:5000])
#sub3 = fig1.add_subplot(313)
sub2.quiver(sheep[::10], wolves[::10])
#plt.savefig('fig.pdf')
plt.show()