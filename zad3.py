from runge_kutta import runge_kutta
from Matrix import Matrix

A = Matrix([[0, 1], [-1, 0]])
T = 0.1
t_max = 20

x = Matrix([[1], [1]])

runge_kutta(A=A, t_max=t_max, T=T, x0=x)