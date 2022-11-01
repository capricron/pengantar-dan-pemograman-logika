const pangkat = (a,b) => {
    return a**b;
}

const modulus = (a,b) => {
    return a%b;
}

const samaDengan = (a,b) => {
    return a==b;
}

const lebihBesar = (a,b) => {
    return a>b;
}

const lebihKecil = (a,b) => {
    return a<b;
}

const tidakSama = (a,b) => {
    return a!==b;
}

const perbandingan = (a,b) => {
    console.log(`Nilai A adalah ${a}`)
    console.log(`Nilai B adalah ${b}`)
    console.log(`A pangkat B adalah ${pangkat(a,b)}`)
    console.log(`A modulus B adalah ${modulus(a,b)}`)
    console.log(`A sama dengan B adalah ${samaDengan(a,b)}`)
    console.log(`A lebih besar dari B adalah ${lebihBesar(a,b)}`)
    console.log(`A lebih besar dari B adalah ${lebihKecil(a,b)}`)
    console.log(`A tidak sama dengan B adalah ${tidakSama(a,b)}`)
}

perbandingan(9,2)