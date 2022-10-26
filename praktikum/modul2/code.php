<?php

function input_variable(){
    $input_nama = fopen("php://stdin","r");    
    return trim(fgets($input_nama));
}

$a = input_variable();
echo "Hasil : $a";
?>