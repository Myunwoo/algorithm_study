/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
  const newArr = []
  let curIdx = 0
  while (curIdx + size <= arr.length) {
      newArr.push(arr.slice(curIdx, curIdx+size))
      curIdx += size
  }

  if (curIdx < arr.length) {
      newArr.push(arr.slice(curIdx, arr.length))
  }

  return newArr
};
