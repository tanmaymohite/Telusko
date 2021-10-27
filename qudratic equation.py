from math import sqrt


print('-----------------------------------------------')
print('          Quadratic Equation-Formula method ')
print('-----------------------------------------------')

a = input('\nEnter the value of A: ')
a = int(a)

b = input('Enter the value of B: ')
b = int(b)

c = input('Enter the value of C: ')
c = int(c)

x = (-b+sqrt(b**2-4*a*c))/2 * a
X = (-b-sqrt(b**2-4*a*c))/2 * a

print('\nAns= '+str(x)+' or '+str(X))