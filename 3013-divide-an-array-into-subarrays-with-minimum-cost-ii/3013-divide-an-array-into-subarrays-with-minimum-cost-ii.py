class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        heap_used, heap_unused, used, unused = [], [], defaultdict(int), defaultdict(int)
        s, total_used, ans, = 0, 0, inf
        for right in range(1, len(nums)):
            left = right - dist - 1
            num_left, num_right = nums[left], nums[right]

            # Move the left border of the window
            if left > 0:
                if num_left in used:
                        # If the left element was used in the cost calculation
                        # remove it from the used counter
                    if used[num_left] == 1: del used[num_left]
                    else: used[num_left] -= 1
                    total_used -= 1
                    s -= num_left

                        # Find the smallest unused element
                    while heap_unused and heap_unused[0] not in unused:
                        heappop(heap_unused)

                    if heap_unused: # If it exists, use it to calculate the cost
                        num = heappop(heap_unused)
                        heappush(heap_used, -num)
                        used[num] += 1
                        total_used += 1
                        s += num

                        if unused[num] == 1 : del unused[num] # and remove it from the unused counter
                        else: unused[num] -= 1 
                else:
                        # If the left element was not used in the cost calculation,
                        # remove it from the unused counter
                    if unused[num_left] == 1: del unused[num_left]
                    else: unused[num_left] -= 1

            # Move the right border of the window
            if total_used < k - 1:
                # If less than k-1 elements are used, use the added element to calculate the cost
                heappush(heap_used, -num_right)
                used[num_right] += 1
                total_used += 1
                s += num_right
            else:
                    #Find the largest used element
                while -heap_used[0] not in used:
                    heappop(heap_used)
                
                if num_right < -heap_used[0]:
                        # If it is larger than the element being added to the window, replace it
                    num = -heapreplace(heap_used, -num_right)
                    if used[num] == 1: del used[num]
                    else: used[num] -= 1
                    used[num_right] += 1
                    s += num_right - num

                        # Add the vacated element to the unused element heap
                    heappush(heap_unused, num)
                    unused[num] += 1
                else:
                        # If the element being added to the window is larger than the largest used element, 
                        # place it on the unused element heap
                    heappush(heap_unused, num_right)
                    unused[num_right] += 1

            if left >= 0:
                ans = min(s, ans)
    
        return nums[0] + ans