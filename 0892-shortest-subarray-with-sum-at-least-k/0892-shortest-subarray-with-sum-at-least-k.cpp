
class Solution {
public:
    int shortestSubarray(std::vector<int>& nums, int k) {
        int n = nums.size();
        int ans = INT_MAX;

        // Compute prefix sums
        std::vector<long long> prefixSum(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }

        deque<int> deque;

        for (int i = 0; i <= n; ++i) {
            while (!deque.empty() && prefixSum[i] - prefixSum[deque.front()] >= k) {
                ans = std::min(ans, i - deque.front());
                deque.pop_front();
            }

            while (!deque.empty() && prefixSum[i] <= prefixSum[deque.back()]) {
                deque.pop_back();
            }

            deque.push_back(i);
        }

        return ans == INT_MAX ? -1 : ans;
    }
};