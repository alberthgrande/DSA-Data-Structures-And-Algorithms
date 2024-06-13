function isMonotonic(arr) {
  let isIncreasing = true;
  let isDecreasing = true;
  for (let i = 1; i < arr.length; i++) {
    // if the element is greater than from previous element
    if (arr[i] > arr[i - 1]) {
      isDecreasing = false;
    }
    // if the element is less than from previous element
    if (arr[i] < arr[i - 1]) {
      isIncreasing = false;
    }
  }

  return isIncreasing || isDecreasing;
}

console.log(isMonotonic([1, 3, 2]));
console.log(isMonotonic([1, 1, 1]));
console.log(isMonotonic([6, 5, 4, 4]));
