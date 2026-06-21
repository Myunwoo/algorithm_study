/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    const result = [];

    function dfs(currentArr, depth) {
        for (const item of currentArr) {
            if (Array.isArray(item) && depth > 0) {
                dfs(item, depth - 1);
            } else {
                result.push(item);
            }
        }
    }

    dfs(arr, n);

    return result;
};