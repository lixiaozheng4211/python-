import random
# 方法一 蒙特卡洛方法
def monte_carlo_pi(n):
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = (x ** 2 + y ** 2) ** 0.5
        if distance <= 1:
            inside_circle += 1
    return 4 * inside_circle / n

# 调用函数并传入模拟的点数
num_points = 1000*1000
print("蒙特卡洛方法估算的圆周率:", monte_carlo_pi(num_points))

# 方法二 使用数学公式（莱布尼茨公式）
def leibniz_pi(n_terms):
    pi_approx = 0
    for n in range(n_terms):
        term = (-1) ** n / (2 * n + 1)
        pi_approx += term
    return 4 * pi_approx

# 调用函数并传入计算的项数
num_terms = 100000
print("莱布尼茨公式估算的圆周率{:.6f}:".format( leibniz_pi(num_terms)))

# 方法三 使用幂级数法（马青公式）
def machin_pi(num_terms):
    pi_approx = 16 * (sum((-1)**i * (1/5)**(2*i + 1)/(2*i + 1) for i in range(num_terms))) - 4 * (sum((-1)**i * (1/239)**(2*i + 1)/(2*i + 1) for i in range(num_terms)))
    return pi_approx
# 设置计算的项数
num_terms = 1000
print("马青公式计算的圆周率近似值:{:.6f}".format( machin_pi(num_terms)))