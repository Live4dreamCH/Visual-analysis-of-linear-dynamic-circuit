from fast import Ut
import numpy as np
import matplotlib.pyplot as plt

L = 0.1
C = 15
Uoo = 10
U0 = 3
I0 = 0

fig, ax = plt.subplots(figsize=(10, 5))
t = np.linspace(0, 20, 300)
for r in [0, 0.1, 0.5, 1, 2.0, 5.0]:
    U = [Ut(t=it, L=L, C=C, Uoo=Uoo, U0=U0, I0=I0, R=r).real for it in t]
    U = np.array(U)
    plt.plot(t, U, label="$R = %.1f$" % r)
ax.set_xlabel(r"$t$", fontsize=18)
ax.set_ylabel(r"$U(t)$", fontsize=18)
plt.legend()
plt.show()
