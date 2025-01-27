# 这个文件包含了一些生成信号样本的函数。

import numpy as np


def generate_points(f, x_min, x_max, n_points=1000):
    """
    用于连续信号: 在 [x_min, x_max] 区间内生成 n_points 个点，
    并计算对应的函数值。
    """
    x_arr = np.linspace(x_min, x_max, n_points)
    # 计算 y 值，但要处理除零错误
    # 如果 y 太大，我们认为是无穷大，用 None 表示
    y_arr = []
    for x in x_arr:
        try:
            y = f(x)
            if abs(y) > 1e4:
                y = np.nan
        except ZeroDivisionError:
            y = np.nan
        y_arr.append(y)
    y_arr = np.array(y_arr)
    return x_arr, y_arr


def generate_samples(f, n_min, n_max):
    """
    用于离散信号: 在 [n_min, n_max] 的整数采样点，计算对应的函数值。
    """
    n_arr = np.arange(n_min, n_max + 1)
    y_arr = []
    for n in n_arr:
        try:
            y = f(n)
            if abs(y) > 1e4:
                y = np.nan
        except ZeroDivisionError:
            y = np.nan
        y_arr.append(y)
    y_arr = np.array(y_arr)
    return n_arr, y_arr