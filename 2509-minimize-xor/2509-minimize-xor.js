/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var minimizeXor = function(num1, num2) {
    let a = num1.toString(2).replace(/0/g, '').length;
    let b = num2.toString(2).replace(/0/g, '').length;
    let res = num1;
    for (let i = 0; i < 32; i++) {
        if (a > b && (1 << i) & num1) {
            res ^= 1 << i;
            a--;
        }
        if (a < b && !((1 << i) & num1)) {
            res ^= 1 << i;
            a++;
        }
    }
    return res;
};