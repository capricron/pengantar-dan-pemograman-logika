<?php

function hitung($kode,$jumlah){
    if ($kode == "B001"){
        $harga = 15000;
        return $harga*$jumlah;
    }else if($kode == "B002"){
        $harga = 18000;
        return $harga*$jumlah;
    }else if($kode == "B003"){
        $harga = 24000;
        return $harga*$jumlah;
    }else if($kode == "B004"){
        $harga = 8000;
        return $harga*$jumlah;
    }
}

echo "Total Harga = ".hitung("B001",5);