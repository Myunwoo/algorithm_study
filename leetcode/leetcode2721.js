/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    if (functions.length === 0) {
        resolve([]);
        return;
    }

    let doneCount = 0
    return new Promise((resolve, reject) => {
        const ret = new Array(functions.length)
        for (let i=0; i<functions.length; i++) {
            functions[i]().then((res) => {
                ret[i] = res
                doneCount++
                if (doneCount === functions.length) {
                    resolve(ret)
                }
            }).catch(e => {
                reject(e)
            })
        }
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */