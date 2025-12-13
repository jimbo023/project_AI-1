import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Задача 1: Базовый график
# Создайте линейный график функции y = sin(x) + cos(2x) на интервале [0, 4π] (от 0 до 4π).
#
# Используйте 100 точек
#
# Добавьте заголовок "График функции sin(x) + cos(2x)"
#
# Подпишите оси: "x" и "y"
#
# Включите сетку
#
# Сохраните график как PNG файл с DPI=150

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x) + np.cos(2 * x)

plt.plot(x, y)

plt.title("График функции sin(x) + cos(2x)")
plt.xlabel("x")
plt.ylabel("y")

plt.grid(True)

plt.show()

# plt.savefig("plot.png", dpi=150, bbox_inches="tight")

# Задача 2: Столбчатая диаграмма
# Данные о продажах за неделю:
#
# python
# дни = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
# продажи = [120, 135, 115, 145, 160, 155, 140]
#
# Создайте столбчатую диаграмму:
#
# Цвет столбцов: синий с прозрачностью 0.7
#
# Черная обводка у столбцов
#
# Выведите значения продаж над каждым столбцом
#
# Добавьте горизонтальную линию на уровне среднего значения продаж (красный пунктир)

days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
sales = [120, 135, 115, 145, 160, 155, 140]

bar = plt.bar(days, sales, alpha=0.7, color="blue", edgecolor="black")
plt.bar_label(bar, fmt="%d")

meanSales = np.mean(sales)

plt.axhline(meanSales, color="red", linestyle="--")

plt.show()

# Задача 3: Точечный график с цветовой кодировкой
# Сгенерируйте 50 случайных точек (x, y) в диапазоне [0, 10].
#
# Размер точек должен зависеть от их удаления от центра (0,0): чем дальше от центра, тем больше точка
#
# Цвет точек должен зависеть от значения x (используйте colormap 'viridis')
#
# Добавьте colorbar
#
# Название графика: "Точечный график с размером и цветом"

x = np.random.randint(0, 11, 50)
y = np.random.randint(0, 11, 50)

plt.scatter(x, y, c=x, s=x + y, cmap='viridis')
plt.colorbar()
plt.title("Точечный график с размером и цветом")
plt.show()

# Задача 4: Несколько графиков на одной фигуре
# Создайте фигуру 2×2 с subplots:
#
# Верхний левый: y = x^2 (красная пунктирная линия)
#
# Верхний правый: y = sqrt(x) (зеленая сплошная линия с маркерами 'o')
#
# Нижний левый: y = exp(-x) (синяя линия, заполнить область под графиком)
#
# Нижний правый: Круговая диаграмма с данными: [25, 35, 20, 20] с подписями ['A', 'B', 'C', 'D']
#
# Для всех графиков x ∈ [0, 5] (кроме круговой диаграммы). У каждого графика должен быть свой заголовок.

x = np.arange(0, 6)
fgr, ax = plt.subplots(2, 2, figsize=(10, 10))

ax[0, 0].plot(x, np.power(x, 2), color="red", linestyle="--")
ax[0, 0].set_title("График 1")

ax[0, 1].plot(x, np.sqrt(x), color="green", marker="o")
ax[0, 1].set_title("График 2")

ax[1, 0].plot(x, np.exp(-x), color="blue")
ax[1, 0].fill_between(x, np.exp(-x))
ax[1, 0].set_title("График 3")

yString = ['A', 'B', 'C', 'D']
xInt = [25, 35, 20, 20]

ax[1, 1].pie(xInt, labels=yString, )
ax[1, 1].set_title("График 4")

plt.show()

# Задача 5: Гистограмма с нормальным распределением
# Сгенерируйте 1000 случайных чисел с нормальным распределением (mean=0, std=1).
#
# Постройте гистограмму с 30 корзинами (bins)
#
# Цвет: светло-синий с черной обводкой
#
# Добавьте вертикальные линии:
#
# Среднее значение (красная сплошная линия)
#
# ±1 стандартное отклонение (зеленые пунктирные линии)
#
# Заголовок: "Нормальное распределение (n=1000)"

numbers = np.random.normal(0, 1, 1000)

fig, ax = plt.subplots(figsize=(10, 8))
meanNumbers = np.mean(numbers)
stdNumbers = np.std(numbers)

ax.hist(numbers, bins=30, color="lightblue", edgecolor="black")
ax.axvline(meanNumbers, color="red")
ax.axvline(meanNumbers - stdNumbers, color="green", linestyle="--")
ax.axvline(meanNumbers + stdNumbers, color="green", linestyle="--")
ax.set_title("Нормальное распределение (n=1000)")

plt.show()

# Задача 6: График с аннотациями
# Постройте график функции y = tan(x) на интервале [-π/2 + 0.1, π/2 - 0.1].
#
# Найдите точку максимума на этом интервале
#
# Выделите эту точку красным маркером размером 100
#
# Добавьте аннотацию к этой точке со стрелкой и текстом "Максимум"
#
# Добавьте вертикальные асимптоты (пунктирные серые линии на x = -π/2 и x = π/2)

x = np.linspace(-np.pi / 2 + 0.1, np.pi / 2 - 0.1, 100)
y = np.tan(x)

plt.plot(x, y)

maxIndex = np.argmax(y)
x_Max = x[maxIndex]
y_Max = y[maxIndex]

plt.scatter(x_Max, y_Max, c="red", s=100)

plt.annotate(
    "Максимум",
    xy=(x_Max, y_Max),
    xytext=(x_Max - 1, y_Max + 1),  # где будет текст
    arrowprops=dict(arrowstyle="->")
)

plt.axvline(x=-np.pi / 2, color="gray", linestyle="--")
plt.axvline(x=np.pi / 2, color="gray", linestyle="--")
plt.show()

# Задача 7: График с двумя осями Y
# Создайте график с двумя осями Y для следующих данных:
#
# python
# время = [0, 1, 2, 3, 4, 5]  # часы
# температура = [20, 22, 23, 21, 19, 18]  # градусы Цельсия
# влажность = [45, 50, 55, 60, 65, 70]    # процент
# Левая ось Y: температура (красная линия)
#
# Правая ось Y: влажность (синяя линия)
#
# Добавьте легенду
#
# Подпишите оси

time = [0, 1, 2, 3, 4, 5]
temp = [20, 22, 23, 21, 19, 18]
humidity = [45, 50, 55, 60, 65, 70]

plt.plot(time, temp, color="red", label="температура (цельсия)")
plt.plot(time, humidity, color="blue", label="влажность (%)")
plt.xlabel("time")

plt.legend()
plt.show()

# Задача 8: Boxplot сравнения
# Сгенерируйте 4 набора данных:
#
# Нормальное распределение (mean=0, std=1)
#
# Равномерное распределение (от -2 до 2)
#
# Экспоненциальное распределение (scale=1)
#
# Случайные числа с выбросами (нормальное + случайные выбросы)
#
# Постройте boxplot для сравнения этих распределений.
#
# Подпишите каждую коробку
#
# Добавьте заголовок "Сравнение распределений"
#
# Измените цвет коробок

normData = np.random.normal(0, 1, 100)
rangeData = np.arange(-2, 3)
expData = np.random.exponential(scale=1, size=100)
randomData = np.random.random(100)

fig, ax = plt.subplots(2, 2, figsize=(10, 8))

ax[0, 0].boxplot(normData)
ax[0, 1].boxplot(rangeData)
ax[1, 0].boxplot(expData)
ax[1, 1].boxplot(randomData)

fig.suptitle("Сравнение распределений")
plt.show()

# Задача 9: График с заливкой области
# Создайте график двух функций на интервале [0, 2π]:
#
# y1 = sin(x) (синяя линия)
#
# y2 = cos(x) (красная линия)
#
# Закрасьте область между этими двумя функциями:
#
# Где sin(x) > cos(x) - зеленым цветом
#
# Где cos(x) > sin(x) - желтым цветом
#
# Добавьте легенду с тремя элементами: sin(x), cos(x), и "Разница"

x = np.arange(0, 2 * np.pi, 0.01)

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")

plt.fill_between(x, y1, y2, alpha=0.3, label="sin(x) > cos(x)", where=(y1 > y2), color="green")
plt.fill_between(x, y1, y2, alpha=0.3, label="cos(x) > sin(x)", where=(y2 > y1), color="yellow")
plt.legend()
plt.show()

# Задача 10: Комплексный проект с Pandas
# Создайте DataFrame с данными о студентах:
#
# python
# import pandas as pd
# import numpy as np
#
# np.random.seed(42)
# данные = {
#     'Студент': [f'Студент_{i}' for i in range(1, 21)],
#     'Математика': np.random.randint(50, 100, 20),
#     'Физика': np.random.randint(40, 95, 20),
#     'Химия': np.random.randint(45, 98, 20),
#     'Год_поступления': np.random.choice([2020, 2021, 2022], 20)
# }
# df = pd.DataFrame(данные)
# Создайте фигуру 2×2:0.
#
# Гистограмма оценок по математике
#
# Scatter plot математика vs физика с цветом по химии
#
# Boxplot оценок по всем предметам
#
# Bar chart средних оценок по годам поступления
#
# Добавьте общий заголовок фигуры и сохраните как PDF.

data = {
    'Студент': [f'Студент_{i}' for i in range(1, 21)],
    'Математика': np.random.randint(50, 100, 20),
    'Физика': np.random.randint(40, 95, 20),
    'Химия': np.random.randint(45, 98, 20),
    'Год_поступления': np.random.choice([2020, 2021, 2022], 20)}

df = pd.DataFrame(data)

fig, ax = plt.subplots(2, 2, figsize=(10, 8))

ax[0, 0].hist(df.Математика)
ax[0, 0].set_title("Гистограмма оценок по математике")

ax[0, 1].scatter(df.Математика, df.Физика, c=df.Химия)
ax[0, 1].set_title("Scatter plot математика vs физика с цветом по химии")

ax[1, 0].boxplot([df.Математика, df.Физика, df.Химия])
ax[1, 0].set_title("Оценок по всем предметам")

meanValues = df.groupby("Год_поступления")[["Математика", "Физика", "Химия"]].mean()
meanValues["Общая"] = meanValues.mean(axis=1)
grouped = meanValues.sort_index()
years = grouped.index.astype(str)
values = grouped["Общая"].values

bars = ax[1, 1].barh(years, values)
ax[1, 1].set_title("Bar chart средних оценок по годам поступления")

plt.show()
