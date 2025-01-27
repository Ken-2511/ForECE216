# 这个文件包含了绘图的封装函数

import numpy as np
import matplotlib.pyplot as plt
from _sample import generate_points, generate_samples


# ===============================
# 绘图封装部分
# ===============================

def plot_continuous_signal(x, y,
                           xlabel='t', ylabel='f(t)',
                           title='Continuous Signal',
                           show=True,
                           **kwargs):
    """
    连续信号绘图: 以曲线形式绘制。
    - x, y: 数据点
    - xlabel, ylabel, title: 轴标签和标题
    - show: 是否在函数内部调用 plt.show()
    - kwargs: 传给 plt.plot 的其它可选参数 (比如 color='red', linestyle='--' 等)
    """
    plt.plot(x, y, **kwargs)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    if show:
        plt.show()


def plot_discrete_signal(x, y,
                         xlabel='n', ylabel='x[n]',
                         title='Discrete Signal',
                         use_stem=True,
                         show=True,
                         **kwargs):
    """
    离散信号绘图: 以“隔点”方式绘制。
    - x, y: 数据点(通常 x 为整数)
    - use_stem: True 则使用“stem”图；False 则可用“scatter”或“plot”离散点。
    - kwargs: 传给对应绘图函数的可选参数
    """
    if use_stem:
        # stem图的 basefmt 可以设置基线样式，比如 " " 表示不显示
        plt.stem(x, y, basefmt=" ", **kwargs)
    else:
        # 用散点或折线代替 stem
        plt.scatter(x, y, **kwargs)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    if show:
        plt.show()


# ===============================
# 统一的“封装示例”:
# 可以根据需要调用上面的函数
# ===============================

def plot_function_continuous(f, x_min, x_max, n_points=1000,
                             xlabel='t', ylabel='f(t)', title='Continuous Signal',
                             show=True, **kwargs):
    """
    统一封装：对连续函数 f，在 [x_min, x_max] 上采样并绘图。
    """
    x, y = generate_points(f, x_min, x_max, n_points=n_points)
    plot_continuous_signal(x, y, xlabel, ylabel, title, show=show, **kwargs)


def plot_function_discrete(f, n_min, n_max,
                           xlabel='n', ylabel='x[n]', title='Discrete Signal',
                           show=True, **kwargs):
    """
    统一封装：对离散函数 f，在整数采样 [n_min, n_max] 上取值并绘图。
    """
    x, y = generate_samples(f, n_min, n_max)
    plot_discrete_signal(x, y, xlabel, ylabel, title, show=show, **kwargs)


if __name__ == '__main__':
    pass
