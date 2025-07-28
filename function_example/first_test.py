from function_example.utils import utils

num1 = 24
num2 = 30

# calculate the average value
# analyze if average value is more than 27


utils_common = utils()
avg1 = utils_common.avg_calc(num1, num2)
avg2 = utils_common.avg_calc(34, 23)
if (avg1 > avg2):
    print("avg1 is bigger than avg2")
else:
    print("avg2 is bigger than avg1")


