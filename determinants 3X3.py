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

v1 = input('Value of equation 1: ')
v1 = int(v1)

v2 = input('Value of equation 2: ')
v2 = int(v2)

v3 = input('Value of equation 3: ')
v3 = int(v3)

D1 = a*((e*i)-(f*h))
D2 = -b*((d*i)-(f*g))
D3 = c*((d*h)-(e*g))


D = D1+D2+D3
print('D: '+str(D))

# now code for Dx

Dx1 = v1*((e*i)-(f*h))
Dx2 = -b*((v2*i)-(f*v3))
Dx3 = c*((v2*h)-(v3*e))

Dx = Dx1+Dx2+Dx3

print('Dx: '+str(Dx))

# now code for Dy

Dy1 = a*((v2*i)-(f*v3))
Dy2 = -v1*((d*i)-(g*f))
Dy3 = c*((d*v3)-(g*v2))

Dy = Dy1+Dy2+Dy3
print('Dy: '+str(Dy))

# now code for Dz

Dz1 = a*((e*v3)-(h*v2))
Dz2 = -b*((d*v3)-(g*v2))
Dz3 = v1*((d*h)-(g*e))

Dz = Dz1+Dz2+Dz3

print('Dz: '+str(Dz))

x = Dx/D
print('x:'+str(x))

y = Dy/D
print('y:'+str(y))

z = Dz/D
print('z:'+str(z))

set = [x,y,z]
print(set)