class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        deltas = [(num ^ k) - num for num in nums]
        positives = [d for d in deltas if d >= 0]
        if len(positives) % 2 == 0:
            return sum(nums) + sum(positives)

        maxNegative = max((d for d in deltas if d < 0), default=float("-inf"))
        minPositive = min(positives)

        return sum(nums) + max(
            sum(positives) + maxNegative, sum(positives) - minPositive
        )