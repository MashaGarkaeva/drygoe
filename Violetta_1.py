import math
import numpy as np
def function(x):
  return (math.sin(x/3)**2 + 3**(1/x - 1)/math.sqrt(x**4 - 16)**(1/6))
x_values = np.arange(2, 21, 1)

y_values = [function(x) for x in x_values]

for i, (x, y) in enumerate(zip(x_values, y_values)):
    print("Решение уравнения: ")
    print(y)
    sr = np.mean(y)
    print("Среднее значение функции: ")
    print(sr)
    sqr = np.sqrt(np.mean(np.square(y)))
    print("Среднее квадратичное значение функции: ")
    print(sqr)
    print("-----")