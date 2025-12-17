import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Реализовать
# функцию f(x) = x²

x = np.linspace(-5, 5, 400)

def f(x):
    return x ** 2

y = f(x)

plt.figure()
plt.plot(x, y)
plt.title("f(x) = x^2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()


# Написать
# цикл, который ищет минимум с шагом по градиенту

# Вывести
# результаты и нарисовать график движения точки к минимуму

x_start = 6 # начальная точка
x_current = x_start # текущее положнеие

a = 0.1 # шаг обучения

iteration = 0
iterations = 100
tolerance = 0

def gradient(x):
    return 2 * x

x_history = []

while iteration < iterations:
    x_new = x_current - a * gradient(x_current)
    if abs(x_new - x_current) < tolerance:
        break
    x_current = x_new
    x_history.append(x_new)
    iteration += 1

y = f(x)

fig, axes = plt.subplots(1, 2, figsize=(8, 6))


axes[0].plot(x, y, label='f(x) = x²')
axes[0].scatter(x_history, [f(xi) for xi in x_history], color='red', s=50, alpha=0.6, label='Шаги градиентного спуска')
axes[0].set_title("Функция f(x) = x²")
axes[0].set_xlabel("x")
axes[0].set_ylabel("f(x)")
axes[0].legend()
axes[0].grid(True)


axes[1].plot(range(len(x_history)), x_history, 'o-', color='blue', markersize=4)
axes[1].set_title("Изменение x на каждой итерации")
axes[1].set_xlabel("Номер итерации")
axes[1].set_ylabel("Значение x")
axes[1].axhline(y=0, color='red', linestyle='--', alpha=0.5, label='Минимум (x=0)')
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()