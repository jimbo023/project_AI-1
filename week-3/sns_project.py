import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Задача 1: Базовый барплот
# Дан датафрейм df_product:
#
# python
# import pandas as pd
# df_product = pd.DataFrame({
#     'product': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D'],
#     'city': ['Moscow', 'Moscow', 'Moscow', 'Moscow', 'SPb', 'SPb', 'SPb', 'SPb'],
#     'sales': [120, 140, 160, 180, 90, 110, 130, 150]
# })
# Задача: Построй столбчатую диаграмму (barplot), где по оси X — product, по оси Y — sales. Столбцы для каждого продукта должны
# быть сгруппированы по city (используй параметр hue). Добавь название графика "Продажи по продуктам".

df_product = pd.DataFrame({
    'product': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D'],
    'city': ['Moscow', 'Moscow', 'Moscow', 'Moscow', 'SPb', 'SPb', 'SPb', 'SPb'],
    'sales': [120, 140, 160, 180, 90, 110, 130, 150]
})

sns.barplot(data=df_product, x="product", y="sales", hue="city")
plt.show()

# Задача 2: Пара парных графиков
# Дан датафрейм df_cars (встроенный в seaborn load_dataset('mpg')).
#
# Задача: Построй pairplot только для числовых колонок ['mpg', 'cylinders', 'horsepower', 'weight'].
# Раскрась точки по признаку origin. Убери верхний треугольник графиков (оставь только нижний, включая диагональ).

df_cars = sns.load_dataset('mpg')

sns.pairplot(df_cars, hue="origin", vars=["mpg", "cylinders", "horsepower", "weight"], corner=True)
plt.show()

# Задача 3: Категориальный боксплот + свёртка
# Дан датафрейм df_tips (встроенный load_dataset('tips')).
#
# Задача: Построй boxplot, где по оси X — day, по оси Y — total_bill.
# Добавь разделение по полу (sex) с помощью параметра hue. Установи палитру 'Set2'. Убери легенду
# и размести два боксплота для каждого дня рядом (параметр dodge по умолчанию True, но проверь).

df_tips = sns.load_dataset('tips')

sns.boxplot(x="day", y="total_bill", data=df_tips, hue="sex", legend=False, palette="Set2")
plt.show()

# Задача 4: Heatmap с аннотацией
# Дан датафрейм df_flights (встроенный load_dataset('flights')).

# Задача: Преобразуй данные в "широкий" формат (pivot_table), где индексы — month, колонки — year, значения — passengers.
# Построй тепловую карту (heatmap). Добавь аннотацию чисел в каждую ячейку (fmt='d').
# Используй цветовую палитру 'YlOrRd'.

df_flights = sns.load_dataset('flights')
flights = df_flights.pivot_table(
    index="month",
    columns="year",
    values="passengers"
)
flights = flights.astype(int)
sns.heatmap(flights, annot=True, cmap="YlOrRd", fmt="d")
plt.show()

# Задача 5: Композитный график (subplots)
# Дан датафрейм df_titanic (встроенный load_dataset('titanic')).
#
# Задача: Создай фигуру с двумя графиками по горизонтали (1 строка, 2 колонки, размер фигуры 12x5).
#
# Левый график: scatterplot с age по оси X и fare по оси Y, точки раскрашены по survived.
#
# Правый график: countplot для pclass, раскрашенный по survived (столбцы стоят друг на друге, параметр stacked в countplot?
# Нет, в seaborn для этого нужно указать hue, а столбцы будут расположены рядом по умолчанию; чтобы сделать stacked, нужно использовать pandas и barplot,
# но в нашем случае — просто countplot с hue).
#
# Для правого графика установи dodge=False, чтобы столбцы были друг на друге (это даст stacked-визуализацию в виде соседних столбцов,
# но для настоящего stacked нужно было бы считать проценты; оставь dodge=False).
#
# Добавь общий заголовок над двумя графиками "Анализ выживаемости на Титанике".

df_titanic = sns.load_dataset('titanic')

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

sns.scatterplot(x="age", y="fare", ax=ax[0], hue="survived", data=df_titanic)
sns.countplot(data=df_titanic, x="pclass", hue="survived", dodge=False, ax=ax[1])

fig.suptitle('Анализ выживаемости на Титанике')
plt.show()
