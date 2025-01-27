from _plot import *


def f_periodic(x):
    """
    假设在 [0,1) 定义 f(x) = 1 / (x+1e-6),
    然后令此函数在正轴上以周期 1 延拓。
    若 x < 0，则直接返回 0 (或继续向负方向周期延拓也可)。
    """
    if x < 0:
        return 0
    # 取 x mod 1
    x_mod = x % 1
    return 1.0 / x_mod


# 设置 y 轴范围
plt.ylim(0, 10)
# 调用连续绘图
plot_function_continuous(
    f_periodic,
    x_min=0,
    x_max=3,
    n_points=1000,
    ylabel='f_periodic(x)',
    title='Periodic Extension Example'
)