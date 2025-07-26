// Sliding window with Recursion 
/**
 * @param {string} s
 * @return {string}
 */
var longestNiceSubstring = function(s) {
    if(s.length < 2) return "";

    const strSet = new Set(s);

    for(let i = 0; i < s.length; i++){
        if(strSet.has(s[i].toUpperCase()) && strSet.has(s[i].toLowerCase())) continue;

        const left = longestNiceSubstring(s.slice(0, i));
        const right = longestNiceSubstring(s.slice(i + 1));

        return left.length >= right.length ? left : right;

    }

    return s;
};