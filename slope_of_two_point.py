x1 = input('Enter the value of x1 = ')
x1 = int(x1)

y1 = input('Enter the value of y1 = ')
y1 = int(y1)

x2 = input('Enter the value of x2 = ')
x2 = int(x2)

y2 = input('Enter the value of y2 = ')
y2 = int(y2)

Y = y1-y2
X = x1-x2

print('Y = '+str(Y))
print('X = '+str(X))

D = X*y1
print('D = '+str(D))
T = Y*x1
print('T = '+str(T))
L = T-D
print('L = '+str(L))

if X == -2:
    N = X/X
    N = N + 1
    print(X)

    if X == -3:
        N = X / X
        N = N + 2
        print(X)
#print('\nAns = '+str(Y)+'x'+str(X)+'y'+'-'+str(L)+'='+'0')

