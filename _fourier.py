import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math


def approximate_function(f, T0, N):
    """
    用傅里叶级数逼近函数 f(x)

    参数:
    - f: 目标函数，f(x)
    - T0: 周期
    - N: 傅里叶级数的最高阶数

    返回:
    - approx: 用傅里叶级数表示的逼近函数
    """
    omega0 = 2 * np.pi / T0  # 基本角频率

    # 计算傅里叶系数 c_k
    def compute_ck(k):
        def integrand(t):
            return f(t) * np.exp(-1j * k * omega0 * t)

        integral, _ = quad(integrand, 0, T0)  # 使用数值积分计算
        return integral / T0

    # 储存傅里叶系数
    coefficients = [compute_ck(k) for k in range(-N, N + 1)]

    # 构造逼近函数
    def approx(t):
        result = 0
        for k, ck in zip(range(-N, N + 1), coefficients):
            result += ck * np.exp(1j * k * omega0 * t)
        return np.real(result)  # 取实部作为结果

    # 返回逼近函数和系数
    return approx, coefficients


# 示例: 目标函数
# def target_function(x):
#     return np.abs(np.sin(x))  # 示例函数: |sin(x)|

def target_function(x):
    """
    方波函数
    """
    # 取 x mod 2π
    x_mod = x % (2 * math.pi)
    if x_mod < math.pi:
        return 1
    else:
        return -1

# 参数设置
T0 = 2 * np.pi  # 周期
N = 5  # 傅里叶级数最高阶数

# 获取逼近函数
approx, coeffs = approximate_function(target_function, T0, N)

# 绘制原函数和逼近函数
x = np.linspace(0, 2 * np.pi, 1000)
y_original = target_function(x)
y_approx = [approx(t) for t in x]

plt.figure(figsize=(10, 6))
plt.plot(x, y_original, label="Original Function", linewidth=2)
plt.plot(x, y_approx, label=f"Fourier Approximation (N={N})", linestyle="--")
plt.title("Function Approximation Using Fourier Series")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()
