print('************ 3X3 determinants *************')

a = input('Enter the value of a: ')
a = int(a)

b = input('Enter the value of b: ')
b = int(b)

c = input('Enter the value of c: ')
c = int(c)

d = input('Enter thevalue of d: ')
d = int(d)

e = input('Enter the value of e: ')
e = int(e)

f = input('Enter the value f: ')
f = int(f)

g = input('Enter the value of g: ')
g = int(g)

h = input('Enter the value of h: ')
h = int(h)

i = input('Enter the value of i : ')
i = int(i)

D1 = a*((e*i)-(f*h))
D2 = -b*((d*i)-(f*g))
D3 = c*((d*h)-(e*g))


D = D1+D2+D3

print('Ans: '+str(D))



