/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const ch=[];
    let i=0;
    while(i<arr.length){
        ch.push(arr.slice(i,i+size));
        i+=size;
    }
    return ch;
};
