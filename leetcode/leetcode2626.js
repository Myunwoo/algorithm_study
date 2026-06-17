/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
  let cur = init
  for (const n of nums) {
      cur = fn(cur, n)
  }
  return cur
};