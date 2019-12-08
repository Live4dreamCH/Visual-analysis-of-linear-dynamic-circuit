from cmath import sqrt, exp

# result= Eq(U(t), Uoo + (C*I0*L + (U0 - Uoo)*(C*R + sqrt(C*(C*R**2 - 4*L)))/2)*exp(t*(-R + sqrt(C*(C*R**2 - 4*L))/C)/(2*L))/sqrt(C*(C*R**2 - 4*L)) + (-2*C*I0*L + 2*sqrt(C*(C*R**2 - 4*L))*(U0 - Uoo) - (U0 - Uoo)*(C*R + sqrt(C*(C*R**2 - 4*L))))*exp(t*(-R - sqrt(C*(C*R**2 - 4*L))/C)/(2*L))/(2*sqrt(C*(C*R**2 - 4*L))))
# when R==2*sqrt(L/C),result= (I0*L*t + L*U0 + L*Uoo*exp(t*sqrt(L/C)/L) - L*Uoo + U0*t*sqrt(L/C) - Uoo*t*sqrt(L/C))*exp(-t*sqrt(L/C)/L)/L

'''
L = 1
C = 1
Uoo = 0
U0 = 10
I0 = 0
'''


def Ut(t, U0, I0, L, R, C, Uoo):
    # 计算瞬态电压
    if R == 2 * sqrt(L / C):
        return (I0 * L * t + L * U0 + L * Uoo * exp(t * sqrt(L / C) / L) - L * Uoo + U0 * t * sqrt(
            L / C) - Uoo * t * sqrt(L / C)) * exp(-t * sqrt(L / C) / L) / L
    else:
        return Uoo + (C * I0 * L + (U0 - Uoo) * (C * R + sqrt(C * (C * R ** 2 - 4 * L))) / 2) * exp(
            t * (-R + sqrt(C * (C * R ** 2 - 4 * L)) / C) / (2 * L)) / sqrt(C * (C * R ** 2 - 4 * L)) + (
                           -2 * C * I0 * L + 2 * sqrt(C * (C * R ** 2 - 4 * L)) * (U0 - Uoo) - (U0 - Uoo) * (
                               C * R + sqrt(C * (C * R ** 2 - 4 * L)))) * exp(
            t * (-R - sqrt(C * (C * R ** 2 - 4 * L)) / C) / (2 * L)) / (2 * sqrt(C * (C * R ** 2 - 4 * L)))
