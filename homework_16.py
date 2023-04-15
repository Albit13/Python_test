lst = [3.5, 2, 4, 6.2, 8]
new_lst = [lst[0]]

for i in range(len(lst)-1):
    a = lst[i]
    b = lst[i+1]
    avg = (a + b) / 2
    new_lst.append(avg)
    new_lst.append(b)

print(new_lst)
