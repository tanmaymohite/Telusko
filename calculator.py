print('     +-*/               python calculator               +-*/ ')

funcition = ['1.Addition','2.Substraction','3.Division','4.Multiplication']
for fun in funcition:
    print(fun)

def add():
    a = f+s
    print('\nAns: '+str(a))

def sub():
    su = f-s
    print('\nAns: '+str(su))

def div():
    d = f/s
    print('\nAns: '+str(d))

def multi():
    m = f*s
    print('\nAns: '+str(m))

t = int(input('\nChosse your choice: '))

f = input('\nEnter the first number: ')
f = int(f)

s = input('Enter the second number: ')
s = int(s)



if t==1:
    add()

elif t==2:
    sub()

elif t == 3:
    div()

elif t == 4:
    multi()

