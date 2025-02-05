/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var areAlmostEqual = function(s1, s2) {
    let arr = [...s1], x = -1;
    for (let i = 0; i < s1.length; i++) {
        if (arr[i] !== s2[i]) {
            if (x === -1) x = i;
            else {
                [arr[i], arr[x]] = [arr[x], arr[i]];
                return arr.join('') === s2;
            }
        }
    }
    return s1 === s2;
};