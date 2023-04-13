input_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

divisible_by_3 = []
divisible_by_5 = []
divisible_by_3_and_5 = []

for num in input_lst:
    if num % 3 == 0 and num % 5 != 0:
        divisible_by_3.append(num)
    elif num % 5 == 0 and num % 3 != 0:
        divisible_by_5.append(num)
    elif num % 3 == 0 and num % 5 == 0:
        divisible_by_3_and_5.append(num)

print(divisible_by_3)
print(divisible_by_5)
print(divisible_by_3_and_5)
