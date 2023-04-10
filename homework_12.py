# s = input('Enter your phrase: ')
s = "aab qq c badcc a qqqqqaqqqqaa tpara"
words = s.split()
result = ""
for word in words:
    if word.count('a') == 2:
        result += word + " "
result = result.title()
print(result)
