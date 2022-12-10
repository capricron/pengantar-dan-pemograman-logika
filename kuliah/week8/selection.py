a = [64,34,25,102,22,11,92]

# selection sort
for i in range(len(a)):
    min = i
    for j in range(i+1, len(a)):
        if a[min] > a[j]:
            min = j
    a[i], a[min] = a[min], a[i]

print(a)