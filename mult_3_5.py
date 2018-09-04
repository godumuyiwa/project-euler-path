value = int(input('Enter the value:'))
def mult():
    mult_3_5 = 0
    for t in range(0,value,3):
        if t%5 == 0:
            continue
        else:
            mult_3_5 += t
    for k in range(0,value,5):
        mult_3_5 += k
    return mult_3_5
print('The Sum of multiples of 3 and 5 below {0} is {1}'.format(value, mult()))