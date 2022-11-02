<?php

function kode($kode){
    $shift = substr($kode,0,2);
    $bidang = substr($kode,2,2);
    
    if($shift == "ML"){
        $shift = "Malam";
    }else if($shift == "PG"){
        $shift = "Pagi";
    }else if($shift == "SG"){
        $shift = "Siang";
    }else if($shift == "LB"){
        $shift = "Lembur";
    }

    if($bidang == "KU"){
        $bidang = "Keuangan";
    }elseif($bidang == "AD"){
        $bidang = "Administrasi";
    }elseif($bidang == "IT"){
        $bidang = "Information Technology";
    }elseif($bidang == "GD"){
        $bidang = "Gudang";
    }

    echo "Shift : $shift \n";
    echo "Bidang : $bidang \n";
}

kode("PGIT");