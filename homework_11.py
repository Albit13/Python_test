multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."

sentences = multi_string.split(".")

words_number = []

for sentence in sentences:
    words = sentence.strip().split(" ")
    count = 0
    for word in words:
        if word:
            count += 1
    if count > 0:
        words_number.append(count)

print(words_number)
