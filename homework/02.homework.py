# set the list of 8 numbers and print whether they are couple or not
x = [15, 56, 5, 8, 42, 22, 11, 20]
for num in x:
    if num % 2 == 0:
        print(f'the {num} is a couple number')
    else:
        print(f'the {num} is not a couple number')

# set the list of emails and check whether they are legal or not
# emails = ['john@gmail.com', 'sara.outlook.com', 'daviddomain.org' ]
# for email in emails:
#     if '@' in email:
#         print(f'the {email} is a legal email')
#     else:
#         print(f'the {email} is an illegal email')

# set a list of numbers, print if sum+num>10 or sum=num<10 of number
# my_list = [1, 1, 1, 2, 6, 0, 28]
# sum = 0
# for list_plus_num in my_list:
#     if list_plus_num == 0:
#         break
#     else:
#         sum = sum + list_plus_num
#         if sum > 10:
#             print(f'the {sum} is bigger than 10')
#         else:
#             if sum < 10:
#                 print(f'the {sum} is less than 10')
#             else:
#                 print(f'the {sum} is 10 ')


# set 5 different ages. print if age between 0-18, 19-60 or 61-120
# age = 68
# if 0 <= age <= 18:
#     print('child')
# elif 19 <= age <= 60:
#     print('adult')
# elif 61 <= age <= 120:
#     print('senior')
