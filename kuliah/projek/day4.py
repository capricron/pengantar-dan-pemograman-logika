#Silahkan masukkan jawaban day-1 mulai dari bagian di bawah ini
namaBarang_1 = input("Masukkan Nama Barang Pertama: ")
kodeBarang_1 = input("Masukkan Kode Barang Pertama: ")
hargaBarang_1 = float(input("Masukkan Harga Barang Pertama: "))
jumlahBarang_1 = int(input("Masukkan Jumlah Barang Pertama: "))
diskonBarang_1 = float(input("Masukkan Diskon Barang Pertama: "))

namaBarang_2 = input("Masukkan Nama Barang Kedua: ")
kodeBarang_2 = input("Masukkan Kode Barang Kedua: ")
hargaBarang_2 = float(input("Masukkan Harga Barang Kedua: "))
jumlahBarang_2 = int(input("Masukkan Jumlah Barang Kedua: "))
diskonBarang_2 = float(input("Masukkan Diskon Barang Kedua: "))

namaBarang_3 = input("Masukkan Nama Barang Ketiga: ")
kodeBarang_3 = input("Masukkan Kode Barang Ketiga: ")
hargaBarang_3 = float(input("Masukkan Harga Barang Ketiga: "))
jumlahBarang_3 = int(input("Masukkan Jumlah Barang Ketiga: "))
diskonBarang_3 = float(input("Masukkan Diskon Barang Ketiga: "))

# Ini adalah batas akhir jawaban day-1 !!!!
# Silahkan masukkan jawaban day-4 mulai dari bagian di bawah ini
kalimat = "\n=======================================\nNama Brg | Jml | Total Harga |\n"

keranjang = []
keranjang.append(kodeBarang_1)
keranjang.append(kodeBarang_2)
keranjang.append(kodeBarang_3)

harga = []
diskonsatuan = []

while True :
    pembelian_barang = input()
    if pembelian_barang == kodeBarang_1 :
        jmlh_beli_barang1 = int(input())
        totalharga_1 = jmlh_beli_barang1 * hargaBarang_1
        harga.append(totalharga_1)
        kalimat += f"{namaBarang_1} | {jmlh_beli_barang1} | {totalharga_1} |\n"
        if "DT" or "RT" in pembelian_barang:
            if jmlh_beli_barang1 > 10:
                    if diskonBarang_1 > 0:
                        diskonLebih1 = ((totalharga_1 * diskonBarang_1)/100)
                        diskonsatuan.append(diskonLebih1)
                        kalimat += f"Diskon item khusus | 1 | -{diskonLebih1} |\n"
    elif pembelian_barang == kodeBarang_2 :
        jmlh_beli_barang2 = int(input())
        totalharga_2 = jmlh_beli_barang2 * hargaBarang_2
        harga.append(totalharga_2)
        kalimat += f"{namaBarang_2} | {jmlh_beli_barang2} | {totalharga_2} |\n"
        if "DT" or "RT" in pembelian_barang:
            if jmlh_beli_barang2 > 10:
                    if diskonBarang_2 > 0:
                        diskonLebih2 = ((totalharga_2 * diskonBarang_2)/100)
                        diskonsatuan.append(diskonLebih2)
                        kalimat += f"Diskon item khusus | 1 | -{diskonLebih2} |\n"
    elif pembelian_barang == kodeBarang_3 :
        jmlh_beli_barang3 = int(input())
        totalharga_3 = jmlh_beli_barang3 * hargaBarang_3
        harga.append(totalharga_3)
        kalimat += f"{namaBarang_3} | {jmlh_beli_barang3} | {totalharga_3} |\n"
        if "DT" or "RT" in pembelian_barang:
            if jmlh_beli_barang3 > 10:
                    if diskonBarang_3 > 0:
                        diskonLebih3 = ((totalharga_3 * diskonBarang_3)/100)
                        diskonsatuan.append(diskonLebih3)
                        kalimat += f"Diskon item khusus | 1 | -{diskonLebih3} |\n"
    else :
        print("Mohon maaf, barang tidak ditemukan")
    
    if pembelian_barang in keranjang :
        beli_lagi = input("Apakah anda ingin menambah barang lagi?(y/n)")
        if beli_lagi == "y" :
            continue
        elif beli_lagi == "n":
            total = sum(harga)
            total_diskon = sum(diskonsatuan)
            if total > 1000000:
                diskonsejuta = total * 0.05
                total_akhir1 = total - diskonsejuta
                print(f"{kalimat}=======================================\nTotal Pembelian       |  {total}  |")
                print(f"Diskon                | - {diskonsejuta}  |\n=======================================")
                print(f"Total Akhir           |  {total_akhir1}  |")
                break
            elif total_diskon > 0:
                total_akhirDiskon = total - total_diskon
                print(f"{kalimat}=======================================\nTotal Pembelian       |  {total_akhirDiskon}  |")
                break
            else:
                print(f"{kalimat}=======================================\nTotal Pembelian       |  {total}  |")
                break
#Ini adalah batas akhir jawaban day-4 !!!!