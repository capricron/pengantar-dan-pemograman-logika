angka = int(input())

i = 2
list = []
while True:

    if i % 2 == 0:
        list.append(i)

    if len(list) == angka:
        break;
    i += 1

print(','.join(map(str,list)))

