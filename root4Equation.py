# 从算法说起：算法是解决某一个问题的基本方案
# 牛顿不动点迭代算法：用于数值计算某个方程的根

error = 1e-4
max_iteration = 1e4

y = 78
x_n = 1
i = 0

while (abs(x_n * x_n - y) > error and i < max_iteration):
    x_n = x_n - (x_n * x_n - y) / (2 * x_n)
    i = i + 1

if (i == max_iteration):
    print("超出迭代范围，未找到根")
else:
    print(f"找到x * x = {y}的根，其值为：{x_n}")
