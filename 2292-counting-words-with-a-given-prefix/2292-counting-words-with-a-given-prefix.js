/**
 * @param {string[]} words
 * @param {string} pref
 * @return {number}
 */
var prefixCount = function(words, pref) {
    let ans = 0;
    const len = pref.length;
    for (let word of words) {
        if (word.length >= len && word.slice(0, len) === pref) {
            ans++;
        }
    }
    return ans;
};