min_width = int(input("Enter min width: "))
max_width = int(input("Enter max width: "))

if min_width > max_width:
    print("Error!: Min width should be less or equal to max width")
    quit()
elif (max_width - min_width) % 2 != 0:
    print("Error!: The difference between max and min width should be even")
    quit()
else:
    for i in range(min_width, max_width+1, 2):
        dmnd = '*' * i
        if i > min_width:
            dmnd = '*' + ' '*(i-2) + '*'
        print(dmnd.center(max_width, ' '))
        if i == max_width:
            for j in range(max_width-2, min_width-1, -2):
                dmnd = '*' * j
                if j > min_width:
                    dmnd = '*' + ' '*(j-2) + '*'
                print(dmnd.center(max_width, ' '))
