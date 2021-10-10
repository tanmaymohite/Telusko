from array import *

cars = ['tata evision','tesla','skoda']

cars[1]='nexon'

for i in cars:
    print(i)

x = len(cars)
print(x)

cars.append('tesla')

for k in cars:
    print(k)
x = len(cars)
print(x)

cars.pop(2)

for f in cars:
    print(f)

cars.remove('nexon')

x = len(cars)
print(x)

for f in cars:
    print(f)

cars.reverse()

print(cars)

