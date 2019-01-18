from Matrix import Matrix
from runge_kutta import runge_kutta
from Trapez import trapez

A = Matrix([[0, 1], [200, -102]])
T = 0.001
t_max = 1

x = Matrix([[1], [-2]])

trapez(A=A, T=T, t_max=t_max, x0=x)
print()
runge_kutta(A=A, T=T, t_max=t_max, x0=x)
