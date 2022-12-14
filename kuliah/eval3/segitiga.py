angka = int(input())
spasi = 0 
for i in range(angka):
    for j in range(spasi):
        print(' ',end='')
    spasi += 1
    for j in range(1,angka+1):
        print(j, end='')
    angka -= 1
    print('')
 