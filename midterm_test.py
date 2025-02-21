from _plot import *


def x(t):
    if t < -2:
        return 0
    if t < -1:
        return -t - 2
    if t < 0:
        return 0
    if t < 1:
        return t
    if t < 2:
        return 2 - t
    return 0


def y(t):
    return x(1 - t)


# 设置 y 轴范围
plt.ylim(-3, 3)

# 调用连续绘图
plot_function_continuous(
    y,
    x_min=-3,
    x_max=3,
    n_points=1000,
    title='y(t)',
    show=False,
    color='r'
)
plot_function_continuous(
    x,
    x_min=-3,
    x_max=3,
    n_points=1000,
    title='x(t)',
    show=False,
    color='b'
)