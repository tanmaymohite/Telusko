from functools import reduce

lst = [2,6,4,3,5,9,8,7,1,3]

even = list(filter(lambda n : n%2==0,lst))

double = list(map(lambda n : n * 2,even ))

sum = reduce(lambda a,b: a+b,double)
print(even)
print(double)
print(sum)