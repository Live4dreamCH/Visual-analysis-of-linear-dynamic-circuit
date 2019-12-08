import numpy as np
import sympy
import matplotlib.pyplot as plt


def apply_ics(sol, ics, x, known_params):
    """
    Apply the initial conditions (ics), given as a dictionary on
    the form ics = {y(0): y0, y(x).diff(x).subs(x, 0): yp0, ...},
    to the solution of the ODE with independent variable x.
    The undetermined integration constants C1, C2, ... are extracted
    from the free symbols of the ODE solution, excluding symbols in
    the known_params list.
    """

    free_params = sol.free_symbols - set(known_params)
    eqs = [(sol.lhs.diff(x, n) - sol.rhs.diff(x, n)).subs(x, 0).subs(ics)
           for n in range(len(ics))]
    sol_params = sympy.solve(eqs, free_params)

    return sol.subs(sol_params)


if __name__ == '__main__':
    # sympy.init_printing(use_unicode=True)
    # 定义符号常量
    t, U0, I0 = sympy.symbols('t,U0,I0')
    L, R, C, Uoo = sympy.symbols('L,R,C,Uoo')
    U = sympy.symbols('U', cls=sympy.Function)

    left = L * C * U(t).diff(t, t) + R * C * U(t).diff(t) + U(t)
    right = Uoo
    eq = sympy.Eq(left, right)
    # print(eq)
    # 调用dsolve函数,返回一个Eq对象，hint控制精度
    eq_solve = sympy.dsolve(eq, U(t))
    # print(eq_solve)
    ics = {U(0): U0, U(t).diff(t).subs(t, 0): I0}
    # print(ics)
    result = apply_ics(eq_solve, ics, t, [L, R, C, Uoo])
    print('result=')
    # sympy.pretty_print(result.rhs)
    print(result.rhs)

    U_t_R = sympy.limit(result.rhs, R, 2 * sympy.sqrt(L / C))
    print('when R==2*sqrt(L/C),result=')
    sympy.pretty_print(U_t_R)

    # U_t_L = sympy.limit(result.rhs, L, 0)
    # print('when L,result=', U_t_L)

    # U_t_C = sympy.limit(result.rhs, C, 0)
    # print('when C,result=', U_t_C)

    fig, ax = plt.subplots(figsize=(8, 4))
    tt = np.linspace(0, 20, 250)
    for r in [0, 0.1, 0.5, 1, 2.0, 5.0]:
        if r == 2:
            U_t = sympy.lambdify(t, U_t_R.subs({U0: 0, I0: 0, L: 1, C: 1, Uoo: 10}), 'numpy')
        else:
            U_t = sympy.lambdify(t, result.rhs.subs({U0: 0, I0: 0, L: 1, C: 1, R: r, Uoo: 10}), 'numpy')
        ax.plot(tt, U_t(tt).real, label="$R = %.1f$" % r)
    ax.set_xlabel(r"$t$", fontsize=18)
    ax.set_ylabel(r"$U(t)$", fontsize=18)
    ax.legend()
    plt.show()
