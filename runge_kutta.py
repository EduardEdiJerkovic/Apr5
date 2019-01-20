from matrix import Matrix
import math
import copy


def real_value(x, t, i):
    x1 = x[0, 0]
    x2 = x[1, 0]

    r1 = x1 * math.cos(t) + x2 * math.sin(t)
    r2 = x2 * math.cos(t) - x1 * math.sin(t)

    print(f"Real: t = {t} X {i}: {Matrix([[r1], [r2]])}")

    return Matrix([[r1], [r2]])


def next_x(A, x, T):
    return A * x + (x + T * A * x)


def runge_kutta(A, B, x0, T=0.01, t_max=0.1, real_value_flag=False):
    print("------------ Method Runge-Kutta ------------")
    f = lambda x: A * x
    m1 = lambda x: f(x) + B
    m2 = lambda x: f(x + T * m1(x) / 2) + B
    m3 = lambda x: f(x + T * m2(x) / 2) + B
    m4 = lambda x: f(x + T * m3(x)) + B
    next_x = lambda x: x + T * (m1(x) + 2 * m2(x) + 2 * m3(x) + m4(x)) / 6

    i = 0
    t = 0
    xr = copy.copy(x0)
    xx = copy.copy(x0)
    print(f"t = {t} X {i}: {xx}")
    while True:
        t += T
        if t >= t_max:
            return
        xx = next_x(xx)
        i += 1
        if i % 1 == 0:
            print(f"t = {t} X {i}: {xx}")
        if real_value_flag:
            xr = real_value(xr, T, i)
