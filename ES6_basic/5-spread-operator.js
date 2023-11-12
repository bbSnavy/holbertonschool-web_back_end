export default function concatArrays(array1, array2, string) {
  let result = [];

  for (let i = 0; i < array1.length; i++) {
    result.push(array1[i]);
  }

  for (let i = 0; i < array2.length; i++) {
    result.push(array2[i]);
  }

  for (let i = 0; i < string.length; i++) {
    result.push(string[i]);
  }

  return result;
}
