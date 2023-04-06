height = int(input("Enter rectangle height: "))
width = int(input("Enter rectangle width: "))
symbol = input("Enter symbol to build rectangular with: ")
for i in range(height):
    row = symbol * width
    print(row, end="")
    if i != height - 1:
        print()