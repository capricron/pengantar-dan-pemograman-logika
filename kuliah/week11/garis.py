angka = int(input())

list = []

for i in range(1,angka+1):
    list.append(i)

print('|'.join(map(str,list)))