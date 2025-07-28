num1 = 5
num2 = 10
num3 = 21
modulo = num3 % num1  # trace of num3 that can't be divided to make integer as answer

summary = num1 + num2
result = num2 - num1
multiple = num1 * num2
dived_by_float = num3 / num1 # the answer is float even though it has no trace
dived_by_int = num3 // num1 # only integer with no trace
print(dived_by_float)
print(dived_by_int)
print(modulo)

summary_as_str = str(summary)  # casting - converting from int to string
num_as_str = '20'
num_as_str = int(num_as_str)  # convertion from string to int
print(num_as_str)

print('test end')
