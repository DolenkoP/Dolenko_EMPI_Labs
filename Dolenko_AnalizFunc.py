# Нормальний закон

import matplotlib.pyplot as plt
import numpy as np
import math

TABLVALUE = 2.26
changes = True
n = 7
np.random.seed()
#генерування елементів за нормальним законом функції
x = 2+np.random.normal(2, 1.5, n)

print(x)

maxValue = x.max()
print(maxValue)
minValue = x.min()
print(minValue)
averageValue = sum(x)/n
print(averageValue)
firstValue = sum((i-averageValue)**2 for i in range(n))/n

SecondVlaue = n*firstValue/(n-1)
print(SecondVlaue)
print((maxValue-averageValue)/SecondVlaue)
print((averageValue-minValue)/SecondVlaue)

fig, ax = plt.subplots()
ax.plot(x,marker="o",linestyle='')
plt.show()

while changes:
    if(((maxValue-averageValue)/SecondVlaue)>TABLVALUE):
        x.max = averageValue
        maxValue = max(x)
        changes = True
    else:   
        changes=False
    if(((averageValue-minValue)/SecondVlaue)>TABLVALUE):
        x.min = averageValue
        minValue = min(x)
        changes = True
    else:   
        changes=False
    ax.plot(x,marker="o",linestyle='')   
    plt.show()

fig, ax = plt.subplots()

ax.plot(x,marker="o",linestyle='')
plt.show()
