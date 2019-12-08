import numpy as np
import matplotlib.pyplot as plt
from math import exp


def ft(t, f0, foo, tao):
    if t > 0:
        return foo + (f0 - foo) * exp(-t / tao)
    else:
        return f0


if __name__ == '__main__':
    Uoo = 10
    U0 = 5
    tao = 5
    t = np.linspace(-20, 20, 200)
    U = [ft(t=it, f0=U0, foo=Uoo, tao=tao) for it in t]
    U = np.array(U)
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.plot(t, U)
    ax.set_xlabel(r"$t$", fontsize=18)
    ax.set_ylabel(r"$U(t)$", fontsize=18)
    # plt.legend()
    plt.show()
