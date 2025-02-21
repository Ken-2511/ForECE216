import math
from _fourier import *


# 定义 x(t)
def x_t(t):
    if t < -2:
        return x_t(t + 4)
    if t > 2:
        return x_t(t - 4)
    if t < -1:
        return -t - 2
    if t < 1:
        return t
    return -t + 2


# 绘制 C_k 随 k 的变化
k_values = np.arange(-10, 11)
C_values = [compute_Ck(x_t, -4, 4, k) for k in k_values]
from _plot import plot_discrete_signal

plot_discrete_signal(
    k_values,
    [C.real for C in C_values],
    title='C_k vs. k',
    xlabel='k',
    ylabel='C_k.real',
)

plot_discrete_signal(
    k_values,
    [C.imag for C in C_values],
    title='C_k vs. k',
    xlabel='k',
    ylabel='C_k.imag',
)