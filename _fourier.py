import numpy as np
import scipy.integrate as spi


def compute_Ck(x_t, T0, T1, k):
    """
    计算连续时间傅里叶级数 (CTFS) 系数 C_k

    参数：
    - x_t: 目标函数 (lambda function)
    - T0, T1: 积分区间
    - k: 计算的谐波索引

    返回：
    - C_k: 计算的傅里叶级数系数
    """
    T = T1 - T0  # 计算周期
    omega_0 = 2 * np.pi / T  # 计算基频

    # 被积函数
    integrand = lambda t: x_t(t) * np.exp(-1j * k * omega_0 * t)

    # 计算积分
    C_k, _ = spi.quad(lambda t: integrand(t).real, T0, T1)  # 仅计算实部
    C_k_imag, _ = spi.quad(lambda t: integrand(t).imag, T0, T1)  # 计算虚部

    C_k = (C_k + 1j * C_k_imag) / T  # 归一化

    return C_k


if __name__ == '__main__':
    # 定义 x(t) 方波信号
    # x_t = lambda t: 1 if 0 <= t < 1 else -1
    def x_t(t):
        if t < -1:
            return -t - 2
        if t < 1:
            return t
        return -t + 2

    # 计算 C_k, k=1
    C_1 = compute_Ck(x_t, -2, 2, 1)
    print(f"C_1 = {C_1}")

    # 绘制 C_k 随 k 的变化
    k_values = np.arange(-10, 11)
    C_values = [compute_Ck(x_t, -2, 2, k) for k in k_values]
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