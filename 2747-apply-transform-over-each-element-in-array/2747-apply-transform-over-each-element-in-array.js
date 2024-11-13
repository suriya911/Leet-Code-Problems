/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const newArr = [];
    arr.forEach((ele,i) =>{
        newArr[i] = fn(ele,i);
    });
    return newArr;
};