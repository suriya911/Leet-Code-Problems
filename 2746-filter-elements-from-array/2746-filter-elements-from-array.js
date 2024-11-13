/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const newArr=[]
    var n=0
    arr.forEach((ele,i) => {
        if(fn(ele,i)){
            newArr[n++]=ele;
        }
    });
    return newArr;
};