class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(inf)

        left = [-1] * (n + 1)
        right = [i + 1 for i in range(n + 1)]
        for i in range(1, n + 1):
            left[i] = i - 1

        heap = [(a + b, i) for i, (a, b) in enumerate(pairwise(nums))]
        heapify(heap)

        rest = sum(1 for a, b in pairwise(nums) if a > b)
        ans = 0

        while rest > 0:
            v, i = heappop(heap)
            r = right[i]

            if r == -1 or nums[i] + nums[r] != v or left[r] != i:
                continue

            rr = right[r]

            if left[i] != -1 and nums[left[i]] > nums[i]:
                rest -= 1
            if nums[i] > nums[r]:
                rest -= 1
            if rr != -1 and nums[r] > nums[rr]:
                rest -= 1

            nums[i] = v
            right[i] = rr
            if rr != -1:
                left[rr] = i

            if left[i] != -1 and nums[left[i]] > nums[i]:
                rest += 1
            if rr != -1 and nums[i] > nums[rr]:
                rest += 1

            if left[i] != -1:
                heappush(heap, (nums[left[i]] + nums[i], left[i]))
            if rr != -1:
                heappush(heap, (nums[i] + nums[rr], i))

            ans += 1

        return ans
