#Silahkan masukkan jawaban day-1 mulai dari bagian di bawah ini
namaBarang_1 = input("Masukkan Nama Barang1: ")
kodeBarang_1 = input("Masukkan Kode Barang1: ")
hargaBarang_1 = float(input("Masukkan Harga Barang1: "))
jumlahBarang_1 = int(input("Masukkan Jumlah Barang1: "))
diskonBarang_1 = float(input("Masukkan Diskon Barang1: "))
namaBarang_2 = input("Masukkan Nama Barang2: ")
kodeBarang_2 = input("Masukkan Kode Barang2: ")
hargaBarang_2 = float(input("Masukkan Harga Barang2: "))
jumlahBarang_2 = int(input("Masukkan Jumlah Barang2: "))
diskonBarang_2 = float(input("Masukkan Diskon Barang2: "))
namaBarang_3 = input("Masukkan Nama Barang3: ")
kodeBarang_3 = input("Masukkan Kode Barang3: ")
hargaBarang_3 = float(input("Masukkan Harga Barang3: "))
jumlahBarang_3 = int(input("Masukkan Jumlah Barang3: "))
diskonBarang_3 = float(input("Masukkan Diskon Barang3: "))

#Ini adalah batas akhir jawaban day-1 !!!!
#Silahkan masukkan jawaban day-3 mulai dari bagian di bawah ini
tulisanPembelian = ""
def askAgain():
        pembelian_lagi = input("Apakah anda ingin menambah barang lagi?(y/n): ")
        if pembelian_lagi == "y":
            return True
        else:
            return False

while True:
    pembelian_barang = input("")
    if pembelian_barang == kodeBarang_1:
        jmlh_beli_barang = int(input())
        tulisanPembelian += (f"{namaBarang_1} | {jmlh_beli_barang} | {jmlh_beli_barang * hargaBarang_1} |")
        if askAgain():
            tulisanPembelian += "\n"
            continue
        else:
            break
    elif pembelian_barang == kodeBarang_2:
        jmlh_beli_barang = int(input())
        tulisanPembelian += (f"{namaBarang_2} | {jmlh_beli_barang} | {jmlh_beli_barang * hargaBarang_2} |")
        if askAgain():
            tulisanPembelian += "\n"
            continue
        else:
            break
    elif pembelian_barang == kodeBarang_3:
        jmlh_beli_barang = int(input())
        tulisanPembelian += (f"{namaBarang_3} | {jmlh_beli_barang} | {jmlh_beli_barang * hargaBarang_3} |")
        if askAgain():
            tulisanPembelian += "\n"
            continue
        else:
            break
    else:
        print("Mohon maaf, barang tidak ditemukan")

print("=======================================")
print("Nama Brg | Jml | Total Harga |")
print(tulisanPembelian)
print("=======================================")
#Ini adalah batas akhir jawaban day-3 !!!!