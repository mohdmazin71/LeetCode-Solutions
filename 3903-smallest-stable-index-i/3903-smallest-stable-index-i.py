class Solution:
    def firstStableIndex(self, nums, k):
        mn = nums[-1]
        suffix = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            mn = min(mn, nums[i])
            suffix[i] = mn

        mx = nums[0]

        for i in range(len(nums)):
            mx = max(mx, nums[i])
            if mx - suffix[i] <= k:
                return i

        return -1