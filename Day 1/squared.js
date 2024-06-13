let arrays = [10, 20, 30, 40, 50];
console.log(arrays);
function takesArrays(arrays) {
  let storedArrays = [];
  for (let i = 0; i < arrays.length; i++) {
    let arraysSquare = (arrays[i] *= arrays[i]);
    storedArrays.push(arraysSquare);
  }
  storedArrays.sort((a, b) => a - b);
  return storedArrays;
}

let squaredArrays = takesArrays(arrays);
console.log(squaredArrays);
