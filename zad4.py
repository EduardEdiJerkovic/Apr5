from matrix import Matrix
from runge_kutta import runge_kutta
from trapez import trapez

if __name__ == '__main__':
    A = Matrix([[0, 1], [-200, -102]])
    B = Matrix([[0], [0]])
    T = 0.1
    t_max = 0.5

    x = Matrix([[1], [-2]])

    trapez(A=A, B=[], T=T, t_max=t_max, x0=x)
    print()
    runge_kutta(A=A, B=B, T=T, t_max=t_max, x0=x,)

