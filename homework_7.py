size = int(input("Enter size of triangle: "))
for i in range(1, size+1):
    spaces = " " * (size - i)
    signs = "*" * i
    print(spaces + signs, end="")
    if i != size:
        print()