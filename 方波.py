from _plot import *
import math


def square_wave(x):
    """
    方波函数
    """
    # 取 x mod 2π
    x_mod = x % (2 * math.pi)
    if x_mod < math.pi:
        return 1
    else:
        return -1

# 设置 y 轴范围
plt.ylim(-2, 2)

# 调用连续绘图
plot_function_continuous(
    square_wave,
    x_min=0,
    x_max=10,
    n_points=1000,
    title='Square Wave'
)

# # 调用离散绘图
# plot_function_discrete(
#     square_wave,
#     n_min=0,
#     n_max=10,
#     title='Square Wave'
# )