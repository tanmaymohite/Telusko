num = input('Enter the number : ')
num = int(num)

for n in range(2,num):
    if num % n == 0:
        print('Not prime')
        break


else:
    print('Prime')

