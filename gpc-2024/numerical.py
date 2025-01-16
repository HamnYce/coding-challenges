def f(x):
    return x**3 + 4 * x**2 - 10


def bisection(f, a, b, eps):
    for i in range(100):
        fa = f(a)
        fb = f(b)

        if fa * fb > 0:
            print("not possible with current bounds")
            return

        p = (a + b) * 0.5
        fp = f(p)

        if abs(fp) <= eps:
            print("the root is", p)

        if fa * fp < 0:
            b = p
        elif fb * fp < 0:
            a = p
        print(f"it {i}, fp: {fp}")


bisection(f, 1, 2, 1e-4)
