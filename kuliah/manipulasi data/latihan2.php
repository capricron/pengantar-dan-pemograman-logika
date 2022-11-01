<?php

function pangkat($a,$b){
    $hasil = $a ** $b;
    return $hasil;
}

function modulus($a,$b){
    $hasil = $a % $b;
    return $hasil;
}

function samaDengan($a,$b){
    $hasil = $a == $b;
    return $hasil;
}

function lebihBesar($a,$b){
    $hasil = $a > $b;
    return $hasil;
}

function lebihKecil($a,$b){
    $hasil = $a < $b;
    return $hasil;
}

function tidakSama($a,$b){
    $hasil = $a != $b;
    return $hasil;
}

function perbandingan($a,$b){
    echo "Nilai A adalah $a \n";
    echo "Nilai B adalah $b \n";
    echo "A pangkat B adalah ". pangkat($a,$b)."\n";
    echo "A modulus B adalah ". modulus($a,$b)."\n";
    echo "A sama dengan B adalah ". (samaDengan($a,$b) ? "true" : "false")."\n";
    echo "A lebih besar dari B adalah ". (lebihBesar($a,$b) ? "true" : "false")."\n";
    echo "A lebih besar dari B adalah ". (lebihKecil($a,$b) ? "true" : "false")."\n";
    echo "A tidak sama dengan B adalah ". (tidakSama($a,$b) ? "true" : "false")."\n";
}

perbandingan(9,2);

?>