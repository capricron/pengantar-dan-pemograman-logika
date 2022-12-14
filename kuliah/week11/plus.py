angka = int(input())
spasi = 0 
for i in range(angka):
    for j in range(spasi):
        print('+',end='')
    spasi += 1
    for j in range(angka, 0, -1):
        print(j, end='')
    angka -= 1
    print('')
 