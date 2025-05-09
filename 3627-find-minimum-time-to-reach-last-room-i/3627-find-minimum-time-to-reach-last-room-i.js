/**
 * @param {number[][]} moveTime
 * @return {number}
 */
var minTimeToReach = function(moveTime) {
    const m = moveTime.length, n = moveTime[0].length;
    const dist = Array.from({ length: m }, () => Array(n).fill(Infinity));
    const heap = [[0, 0, 0]]; // time, row, col
    dist[0][0] = 0;

    const dirs = [[-1,0],[1,0],[0,-1],[0,1]];

    while (heap.length > 0) {
        heap.sort((a, b) => a[0] - b[0]);
        const [time, r, c] = heap.shift();
        if (r === m - 1 && c === n - 1) return time;

        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr >= 0 && nc >= 0 && nr < m && nc < n) {
                const nextTime = Math.max(time, moveTime[nr][nc]) + 1;
                if (nextTime < dist[nr][nc]) {
                    dist[nr][nc] = nextTime;
                    heap.push([nextTime, nr, nc]);
                }
            }
        }
    }
    return -1;
};