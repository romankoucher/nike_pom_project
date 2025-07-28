# first num  = start (5)
# second num  = end (20) not included !!!
# last num  = step (2) # i = i + 2
# THE FORMULA OF RANGE: for i in range (start, stop (not included), i = i + number)
# If I put only one number like 'in range(5)' it will start from 0 till 4
from qa09.int_actions import result

# for i in range (5,20,2): #  i = from 5 till 20 but not included, i = i + 2
#     print(i)
#     result = i * 2
#     print(result) # the result is not depend of i, it can be more than i


# for i in range(1, 11):  # multiply table of 5 from i = 1 till i = 10
#     print(f'referance number is {i}')
#     result = i * 5
#     print(f'the result is {result}')
# print("test end")

name = 'LeoMessi'
is_long = False
cntr = 0
if(len(name)>4):
    is_long = True
    while(is_long):
        print('long name found')
        is_long = True
        cntr = cntr+1
        if(cntr==5):
            break # Getting out of the loop



