jumlahTransaksi = int(input())

hasilPenjualan = 0
for i in range(jumlahTransaksi):
    jualBeliSaham = input().split()
    hargaBeli = int(jualBeliSaham[0])
    hargaJual = int(jualBeliSaham[1])

    total = hargaJual - hargaBeli
    hasilPenjualan += total

print(hasilPenjualan * 100)