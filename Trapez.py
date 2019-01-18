from Matrix import Matrix
import math
import copy


def trapez(A=Matrix([[0, 0], [0, 0]]), B=Matrix([[0, 0], [0, 0]]), x0=Matrix([[0], [0]]), T=0.01, t_max=0.1,):
    print("------------ Metoda Trapez ------------")
    R = Matrix.inverz(Matrix.getI(A.columns_count()) - A * T / 2) * (Matrix.getI(A.columns_count()) + A * T / 2)
    next_x = lambda x: R * x
    i = 0
    t = T
    x = copy.copy(x0)
    print("SIMU t =", t, "X" + str(i) + ":", x)
    while(True):
        t += T
        if (t >= t_max):
            return
        x = next_x(x)
        i += 1
        if (i % 10 == 0):
            print("SIMU t =", t, "X" + str(i) + ":", x)

"""def trapez2(A=Matrix([[0, 0], [0, 0]]), B=Matrix([[0, 0], [0, 0]]), x0=Matrix([[0], [0]]), T=0.01, t_max=0.1):
    print("------------ Metoda Trapez 2 ------------")
    i = 0
    t = T
    x = copy.copy(x0)
    xk11 = x[0, 0] + T * x[1, 0]
    xk21 = x + T
    xk = x  T * x[1, 0]"""

 