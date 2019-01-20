from matrix import Matrix, get_i
import copy


def trapez(A, B, x0, T=0.01, t_max=0.1):
    print("------------ Method Trapez ------------")
    R = Matrix.inverse(get_i(A.columns_count()) - A * T / 2) * (get_i(A.columns_count()) + A * T / 2)
    i = 0
    t = 0
    x = copy.copy(x0)
    print(f"t = {t} X {i}: {x}")
    while True:
        t += T
        if t >= t_max:
            return
        x = R * x
        i += 1
        if i % 1 == 0:
            print(f"t = {t} X {i}: {x}")
            # print("SIMU t =", t, "X" + str(i) + ":", x)
