class Solution:
    def minOperations(self, nums, x):
        target = sum(nums) - x

        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        left = total = ans = 0

        for right in range(len(nums)):
            total += nums[right]

            while total > target:
                total -= nums[left]
                left += 1

            if total == target:
                ans = max(ans, right - left + 1)

        return len(nums) - ans if ans else -1