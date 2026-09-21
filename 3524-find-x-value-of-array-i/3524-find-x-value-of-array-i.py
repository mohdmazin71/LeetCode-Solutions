class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for n in nums:
            x = n % k
            ndp = [0] * k
            ndp[x] = 1

            for r in range(k):
                ndp[r * x % k] += dp[r]

            for r in range(k):
                ans[r] += ndp[r]

            dp = ndp

        return ans