from Matrix import Matrix
import math
import copy

def real_value(x, t, i):
    x1 = x[0, 0]
    x2 = x[1, 0]

    r1 = x1 * math.cos(t) + x2 * math.sin(t)
    r2 = x2 * math.cos(t) - x1 * math.sin(t)

    print("REAL t =", t, "X" + str(i) + ":", Matrix([[r1], [r2]]))
    return Matrix([[r1], [r2]])

def runge_kutta(A=Matrix([[0, 0], [0, 0]]), B=Matrix([[0, 0], [0, 0]]), x0=Matrix([[0], [0]]), T=0.01, t_max=0.1, real_value=False):
    print("------------ Metoda Runge-Kutta ------------")
    f = lambda x: A * x
    m1 = lambda x: f(x)
    m2 = lambda x: f(x + T * m1(x) / 2)
    m3 = lambda x: f(x + T * m2(x) / 2)
    m4 = lambda x: f(x + T * m3(x))
    next_x = lambda x: x + T * (m1(x) + 2 * m2(x) + 2 * m3(x) + m4(x)) / 6

    i = 0
    t = T
    xr = copy.copy(x0)
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
        if (real_value):
            xr = real_value(xr, t, i)



