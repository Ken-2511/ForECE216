from _plot import *
import math


def sine(x):
    """
    正弦函数
    """
    return math.sin(x/5)


# 调用离散绘图
plot_function_discrete(
    sine,
    n_min=0,
    n_max=50,
    title='Discrete Sine Wave'
)