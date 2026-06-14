numbers = []
for i in range(5):
    num = int(input(f"请输入第{i+1}个数字"))
    numbers.append(num)
total =0
for num in numbers:
    total += num
print(total)
average = total/5
print(f"平均值为{average}")
max_num = numbers[0]
for num in numbers[1:]:
    if num > max_num:
        max_num = num
print(f"最大值是{max_num}")
min_num = numbers[0]
for num in numbers[1:]:
    if num < min_num:
        min_num = num
print(f"最小值是{min_num}")
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    if num % 2 != 0:
        odd_numbers.append(num)
print (f"偶数有{even_numbers}")
print (f"奇数有{odd_numbers}")