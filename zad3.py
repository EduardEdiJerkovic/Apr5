from runge_kutta import runge_kutta
from matrix import Matrix
import math

if __name__ == '__main__':
    A = Matrix([[0, 1], [-1, 0]])
    B = Matrix([[0], [0]])
    T = math.pi * 2 / 50
    # T = 0.001
    t_max = 2

    x = Matrix([[1], [1]])

    runge_kutta(A=A, B=B, t_max=t_max, T=T, x0=x, real_value_flag=True)
