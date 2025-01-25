class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        if n == 0:
            return []
        
        # Step 1: Pair each number with its index
        sorted_pairs = sorted([(nums[i], i) for i in range(n)])
        
        result = [0] * n
        group_start = 0
        
        for i in range(n):
            # Step 3: Check if current group ends here
            if i == n - 1 or sorted_pairs[i+1][0] - sorted_pairs[i][0] > limit:
                # Step 4: Collect and sort original indices
                indices = [pair[1] for pair in sorted_pairs[group_start:i+1]]
                indices.sort()
                
                # Step 5: Assign sorted values to sorted indices
                for j in range(len(indices)):
                    result[indices[j]] = sorted_pairs[group_start + j][0]
                
                group_start = i + 1  # Next group
        
        return result