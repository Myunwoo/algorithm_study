/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    const metaArr = []
    const newArr = []
    for (let i=0; i<arr.length; i++) {
        metaArr.push([fn(arr[i]), i])
    }
    metaArr.sort((a, b) => a[0] - b[0])

    for (let i=0; i<arr.length; i++) {
        newArr.push(arr[metaArr[i][1]])
    }
    return newArr
};