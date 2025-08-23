/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumSum = function (grid) {
  let map = new Map();

  function getOne(i1, j1, i2, j2, k) {
    let minx = Infinity;
    let maxx = -Infinity;
    let miny = Infinity;
    let maxy = -Infinity;

    for (let i = i1; i <= i2; i++) {
      for (let j = j1; j <= j2; j++) {
        if (grid[i][j] === 1) {
          minx = Math.min(minx, i);
          maxx = Math.max(maxx, i);
          miny = Math.min(miny, j);
          maxy = Math.max(maxy, j);
        }
      }
    }

    if (minx === Infinity) {
      return 0;
    }

    return (maxx - minx + 1) * (maxy - miny + 1);
  }

  function getNext(i1, j1, i2, j2, k) {
    let key = [i1, j1, i2, j2, k].join();
    if (map.has(key)) {
      return map.get(key);
    }

    let output = Infinity;

    if (k === 1) {
      output = getOne(i1, j1, i2, j2, k);
    } else if (k === 2) {
      for (let i = i1; i < i2; i++) {
        output = Math.min(
          output,
          getNext(i1, j1, i, j2, 1) + getNext(i + 1, j1, i2, j2, 1)
        );
      }
      for (let j = j1; j < j2; j++) {
        output = Math.min(
          output,
          getNext(i1, j1, i2, j, 1) + getNext(i1, j + 1, i2, j2, 1)
        );
      }
    } else if (k === 3) {
      for (let i = i1; i < i2; i++) {
        output = Math.min(
          output,
          getNext(i1, j1, i, j2, 1) + getNext(i + 1, j1, i2, j2, 2)
        );
        output = Math.min(
          output,
          getNext(i1, j1, i, j2, 2) + getNext(i + 1, j1, i2, j2, 1)
        );
      }
      for (let j = j1; j < j2; j++) {
        output = Math.min(
          output,
          getNext(i1, j1, i2, j, 1) + getNext(i1, j + 1, i2, j2, 2)
        );
        output = Math.min(
          output,
          getNext(i1, j1, i2, j, 2) + getNext(i1, j + 1, i2, j2, 1)
        );
      }
    }

    map.set(key, output);
    return output;
  }

  let m = grid.length;
  let n = grid[0].length;

  let ans = getNext(0, 0, m - 1, n - 1, 3);

  return ans;
};