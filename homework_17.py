lst = [['a', 'c', 'd'], ['f', 'b', 'a'], ['a', 'n', 'k'], ['e', 'l', 'i']]
result = [sorted(col) for col in zip(*lst)]
result = list(map(list, zip(*result)))

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print()
