def pangkat(a,b):
    return a**b

def modulus(a,b):
    return a%b

def samaDengan(a,b):
    return a==b

def lebihBesar(a,b):
    return a>b

def lebihKecil(a,b):
    return a<b

def tidakSama(a,b):
    return a!=b

def perbandingan(a,b):
    print(f"Nilai A adalah {a}")
    print(f"Nilai B adalah {b}")
    print(f"A pangkat B adalah {pangkat(a, b)}")
    print(f"A modulus B adalah {modulus(a, b)}")
    print(f"A sama dengan B adalah {samaDengan(a, b)}")
    print(f"A lebih besar dari B adalah {lebihBesar(a, b)}")
    print(f"A lebih besar dari B adalah {lebihKecil(a, b)}")
    print(f"A tidak sama dengan B adalah {tidakSama(a, b)}")

perbandingan(9,2)