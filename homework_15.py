lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
MIN = 3
MAX = 6

sum_ = 0
product = 1

for x in lst:
    if MIN <= x <= MAX:
        sum_ += x
        product *= x

if sum_ == 0 and product == 1:
    print("Sum: 0")
    print("Product: 0")
else:
    print("Sum:", sum_)
    print("Product:", product)
