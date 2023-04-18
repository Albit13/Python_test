max_length = 0
longest_line = ""

with open("D:\\test_file.txt", "r") as f:
    for line in f:
        line = line.strip()
        if len(line) > max_length:
            max_length = len(line)
            longest_line = line

print("Longest line: {}".format(longest_line))