print('     +-*/               python calculator               +-*/ ')

funcition = ['1.Addition','2.Substraction','3.Division','4.Multiplication']
for fun in funcition:
    print(fun)

def add():
    a = f+s
    print('Ans: '+str(a))

def sub():
    su = f-s
    print('Ans: '+str(su))

def div():
    d = f/s
    print('Ans: '+str(d))

def multi():
    m = f*s
    print('Ans: '+str(m))

t = int(input('\nChosse your choice: '))

f = input('\nEnter the first number: ')
f = float(f)

s = input('Enter the second number: ')
s = float(s)



if t==1:
    add()

elif t==2:
    sub()

elif t == 3:
    div()

elif t == 4:
    multi()

