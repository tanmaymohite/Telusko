print('                Factorial program                ')


x = input('\nWhich factorial do you want: ')
x = int(x)


def fact(n):

    f = 1

    for i in range(1,n+1):
        f = f*i

    return f


result = fact(x)

print('Ans =  '+str(result))


