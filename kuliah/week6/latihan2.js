const hitung = (kode,jumlah) => {
    if (kode == "B001"){
        harga = 15000;
    }else if(kode == "B002"){
        harga = 18000;
    }else if(kode == "B003"){
        harga = 24000;
    }else if(kode == "B004"){
        harga = 8000;
    }

    total = harga*jumlah;
    pajak = total*0.11;
    grand = total + pajak;
    
    console.log(`Total = ${total}`)
    console.log(`Pajak = ${pajak}`)
    console.log(`Grand = ${grand}`)
}

hitung("B001",5);