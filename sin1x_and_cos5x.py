from _plot import *
import math


def func(x):
    """
    信号函数
    """
    return math.sin(x) + math.cos(5*x)


# 调用连续绘图
plot_function_continuous(
    func,
    x_min=0,
    x_max=20,
    n_points=1000,
    title='sin(x) + cos(5x)'
)