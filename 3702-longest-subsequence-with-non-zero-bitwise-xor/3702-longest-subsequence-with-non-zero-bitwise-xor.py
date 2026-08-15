class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        if all(x == 0 for x in nums):
            return 0
        
        total_xor = 0
        for num in nums:
            total_xor ^= num
            
        if total_xor != 0:
            return len(nums)
        
        return len(nums) - 1
