# 这个文件包含一些计算范数 (Norm) 的函数

import numpy as np
from _sample import generate_points, generate_samples


def calculate_norm_from_data(x, p=2):
    """
    计算 x 的 p 范数
    """
    return np.linalg.norm(x, ord=p)


def calculate_norm(x, p=2):
    """
    计算 x 的 p 范数
    - x: 输入向量
    - p: 范数的阶数
    """
    return np.power(np.sum(np.power(np.abs(x), p)), 1/p)


if __name__ == '__main__':
    # 测试范数计算
    x = np.array([-3, -1, 0, 1, 2])
    for p in [1, 2, 10, np.inf]:
        print(f'p={p}: {calculate_norm_from_data(x, p)}')