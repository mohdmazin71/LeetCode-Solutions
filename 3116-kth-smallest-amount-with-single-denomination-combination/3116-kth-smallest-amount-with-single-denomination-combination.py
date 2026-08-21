class Solution:
    def findKthSmallest(self, coins, k):
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def ok(x):
            count = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                l = 1

                for i in range(n):
                    if mask >> i & 1:
                        l = l * coins[i] // gcd(l, coins[i])
                        if l > x:
                            break

                else:
                    if mask.bit_count() % 2:
                        count += x // l
                    else:
                        count -= x // l

            return count >= k

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if ok(mid):
                right = mid
            else:
                left = mid + 1

        return left