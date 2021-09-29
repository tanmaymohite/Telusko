def np(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even = even + 1
        else :
            odd = odd + 1

    return even,odd

lst = [25,38,46,25,65,98,73,65,45,41]

even,odd = np(
    lst)

print('even : {} and odd : {}'.format(even,odd))
print('print'+str(lst))
