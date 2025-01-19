import numpy as np

class Solution:

    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        # Fill the water in
        water_level = np.array(heightMap, dtype=int)
        heightMap = np.array(heightMap, dtype=int)
        water_level[1:-1, 1:-1] = np.max(heightMap)

        # Let the water flow out
        w_old = 0
        while True:
            wl_pad = np.pad(water_level, ((1, 1), (1, 1)))
            water_level = np.maximum(np.minimum(np.minimum(wl_pad[0:-2, 1:-1], wl_pad[2:, 1:-1]),
                                                np.minimum(wl_pad[1:-1, 0:-2], wl_pad[1:-1, 2:])), heightMap)
            w = np.sum(water_level - heightMap)
            if w_old == w:
                return int(w)
            w_old = w