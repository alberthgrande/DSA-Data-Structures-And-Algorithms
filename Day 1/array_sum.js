const arr1 = [10, 2, 3, 4];
const arr2 = [1, 27, 33, 45];
let sum = [];
for (let i = 0; i < arr1.length; i++) {
  sum[i] = 0;
  for (let j = 0; j < arr2.length; j++) {
    if (i === j) {
      sum[i] = arr1[i] += arr2[j];
      // sum.push((arr1[i] += arr2[j]));
      break;
    }
  }
}

let total_sum = 0;
for (let i = 0; i < sum.length; i++) {
  total_sum += sum[i];
}

console.log(total_sum);
console.log(sum);
