const mapValues = {
    masculino: {
      1: 60,
      2: 75,
      3: 90,
      4: 85,
      5: 80,
    },
    feminino: {
      1: 60,
      2: 60,
      3: 90,
      4: 85,
      5: 80,
    },
  };
  
  const mapedAges = {
    masculino: [
      { 1: [0, 15] },
      { 2: [16, 18] },
      { 3: [19, 30] },
      { 4: [31, 40] },
      { 5: [41, 0] },
    ],
    feminino: [
      { 1: [0, 15] },
      { 2: [16, 18] },
      { 3: [19, 30] },
      { 4: [31, 40] },
      { 5: [41, 0] },
    ],
  };
  
  const definePrice = (gender, age) => {
    const clienteGenderPricesArr = mapedAges[gender];
  
    for (index = 0; index <= clienteGenderPricesArr.length; index++) {
      if (
        age >= clienteGenderPricesArr[index][index + 1][0] &&
        age <= clienteGenderPricesArr[index][index + 1][1]
      ) {
        return mapValues[gender][index + 1];
      } else if (
        age >= clienteGenderPricesArr[index][index + 1][0] &&
        clienteGenderPricesArr[index][index + 1][1] === 0
      ) {
        return mapValues['5'];
      }
    }
  };
  
  console.log(definePrice('feminino', 26));