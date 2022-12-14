
# angka = int(input())

# x = angka
# for i in range(angka, 0, -1):
#     cetak = ""
#     for j in range(1, i + 1):
#         cetak += str(j)
    
#     cetak += " "
#     cetaks = cetak[::-1]
#     print(cetaks, end="\n")

angka = int(input())
spasi = 0 
for i in range(angka):
    for j in range(spasi):
        print(' ',end='')
    spasi += 1
    for j in range(angka, 0, -1):
        print(j, end='')
    angka -= 1
    print('')
 