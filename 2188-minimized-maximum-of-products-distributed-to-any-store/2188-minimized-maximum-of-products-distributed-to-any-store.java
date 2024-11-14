class Solution {
    public int minimizedMaximum(int n, int[] quantities) {
        int low = 1, high = Integer.MIN_VALUE, res = 0;
        for (int quantity : quantities) {
            high = Math.max(high, quantity);
        }
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int storesNeeded = 0;
            for (int quantity : quantities) {
                storesNeeded += Math.ceil((double) quantity / mid);
            }
            if (storesNeeded <= n) {
                res = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return res;
    }
}