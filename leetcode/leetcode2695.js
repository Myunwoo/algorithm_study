/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.arr = []
    for (const n of nums) {
        this.arr.push(n)
    }
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    let val = 0
    for (const a of this.arr) {
        val += a
    }
    return val
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    if (this.arr.length === 0) {
        return '[]'
    }

    let ret = ''
    for (let i=0; i<this.arr.length-1;i++) {
        ret += String(this.arr[i]) + ','
    }
    ret += this.arr[this.arr.length-1]
    return `[${ret}]`
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */