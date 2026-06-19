var TimeLimitedCache = function() {
    this._memory = new Map();
    this._timerMap = new Map();
    this._count = 0;
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration
 * @return {boolean}
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const alreadyExists = this._memory.has(key);

    if (alreadyExists) {
        clearTimeout(this._timerMap.get(key));
    } else {
        this._count += 1;
    }

    this._memory.set(key, value);

    const timer = setTimeout(() => {
        this._memory.delete(key);
        this._timerMap.delete(key);
        this._count -= 1;
    }, duration);

    this._timerMap.set(key, timer);

    return alreadyExists;
};

/** 
 * @param {number} key
 * @return {number}
 */
TimeLimitedCache.prototype.get = function(key) {
    return this._memory.has(key) ? this._memory.get(key) : -1;
};

/** 
 * @return {number}
 */
TimeLimitedCache.prototype.count = function() {
    return this._count;
};