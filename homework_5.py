#Если заменить int на float - можно ввести число с плавающей точкой
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

if a >= b and a >= c:
    print('Max number:', a)
elif b >= a and b >= c:
    print('Max number:', b)
else:
    print('Max number:', c)