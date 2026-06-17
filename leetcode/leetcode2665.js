/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
  let curVal = init
  const initVal = init

  const increment = () => {
      return ++curVal
  }

  const decrement = () => {
      return --curVal
  }

  const reset = () => {
      curVal = initVal
      return curVal
  }

  return {
      increment,
      decrement,
      reset
  }
};

/**
* const counter = createCounter(5)
* counter.increment(); // 6
* counter.reset(); // 5
* counter.decrement(); // 4
*/