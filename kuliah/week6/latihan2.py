def hitung(kode,jumlah):
    if kode == "B001":
        harga = 15000
    elif kode == "B002":
        harga = 18000
    elif kode == "B003":
        harga = 24000
    elif kode == "B004":
        harga = 8000
    total = harga*jumlah
    pajak = total*0.11
    grand = total + pajak
    print(f"Total = {total}")
    print(f"Pajak = {pajak}")
    print(f"Grand Total = {grand}")

hitung("B001",5)