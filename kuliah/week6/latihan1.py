def hitung(kode,jumlah):
    if kode == "B001":
        harga = 15000
        return harga*jumlah;
    elif kode == "B002":
        harga = 18000
        return harga*jumlah;
    elif kode == "B003":
        harga = 24000
        return harga*jumlah;
    elif kode == "B004":
        harga = 8000
        return harga*jumlah;

print("Total harga =", hitung("B001",5))