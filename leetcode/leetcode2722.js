const setMapWithoutId = (obj, map) => {
    for (const [key, value] of Object.entries(obj)) {
        if (key === 'id') continue
        map.set(key, value)
    }
}

/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const newArr = []
    const map = new Map()

    for (const a1 of arr1) {
        const id = a1.id
        if (map.has(id)) {
            setMapWithoutId(a1, map.get(id))
        } else {
            map.set(id, new Map())
            setMapWithoutId(a1, map.get(id))
        }
    }

    for (const a2 of arr2) {
        const id = a2.id
        if (map.has(id)) {
            setMapWithoutId(a2, map.get(id))
        } else {
            map.set(id, new Map())
            setMapWithoutId(a2, map.get(id))
        }
    }

    for (const [id, valueMap] of map.entries()) {
        const obj = { id };
        for (const [key, value] of valueMap.entries()) {
            obj[key] = value;
        }

        newArr.push(obj);
    }

    newArr.sort((a, b) => a.id - b.id);

    return newArr;
};