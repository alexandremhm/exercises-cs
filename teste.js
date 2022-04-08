const mapValues = {
    '1': 60,
    '2': 75,
    '3': 90,
    '4': 85,
    '5': 80
}


const mapedValues = {
    "masculino": [
        {'1': [0, 15]},
        {'2': [16, 18]},
        {'3': [19, 30]},
        {'4': [31, 40]},
        {'5': [41]},
    ],
    "feminino": [
        {'preço 1': [0, 18]},
        {'preco 3': [19, 25]},
        {'preco 4': [26, 40]},
        {'preco 5': [41]},
    ],
}

const definePrice = (gender, age) => {
    const clienteGenderPricesArr = mapedValues[gender]

    for ( index = 0; index <= clienteGenderPricesArr.length; index ++) {
       if ( age >= clienteGenderPricesArr[index][index + 1][0] || age <= clienteGenderPricesArr[index][index + 1][1]) {
           return mapValues[index + 1]
       }
    }

}

console.log(definePrice("masculino", 18))