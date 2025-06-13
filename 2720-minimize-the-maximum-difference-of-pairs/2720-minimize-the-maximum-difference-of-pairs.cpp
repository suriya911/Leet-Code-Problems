class Solution {
public:
    int minimizeMax(vector<int>& v, int p) {
        int n = v.size();
        sort(v.begin(), v.end()); // Sort the array for minimum differences

        // Binary search for answer
        int lo = -1, hi = 1e9 + 7;
        while (lo < hi - 1) {
            int mid = lo + (hi - lo) / 2;
            int a = 0; // Count of valid pairs
            for (int i = 1; i < n; i++) {
                if (v[i] - v[i - 1] <= mid) {
                    a++;
                    i++; // skip next to avoid overlap
                }
            }
            if (a >= p) hi = mid;
            else lo = mid;
        }
        return hi;
    }
};