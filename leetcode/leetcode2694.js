class EventEmitter {
  constructor() {
      this.eventMap = new Map()
  }
  
  
  /**
   * @param {string} eventName
   * @param {Function} callback
   * @return {Object}
   */
  subscribe(eventName, callback) {
      if (this.eventMap.has(eventName)) {
          this.eventMap.get(eventName).push(callback)
      } else {
          this.eventMap.set(eventName, [callback])
      }
      
      return {
          unsubscribe: () => {
              const handlerArr = this.eventMap.get(eventName)
              const index = handlerArr.indexOf(callback)
              if (index > -1) {
                  handlerArr.splice(index, 1)
              }
          }
      };
  }
  
  /**
   * @param {string} eventName
   * @param {Array} args
   * @return {Array}
   */
  emit(eventName, args = []) {
      if (!this.eventMap.has(eventName)) {
          return []
      }
      const handlerArr = this.eventMap.get(eventName)
      const ret = []
      for (const h of handlerArr) {
          ret.push(h(...args))
      }
      return ret
  }
}

/**
* const emitter = new EventEmitter();
*
* // Subscribe to the onClick event with onClickCallback
* function onClickCallback() { return 99 }
* const sub = emitter.subscribe('onClick', onClickCallback);
*
* emitter.emit('onClick'); // [99]
* sub.unsubscribe(); // undefined
* emitter.emit('onClick'); // []
*/