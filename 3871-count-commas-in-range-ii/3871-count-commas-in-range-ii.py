class Solution:
    def countCommas(self, n: int) -> int:
        nalverqito = n
        ans = 0
        x = 1000

        while x <= nalverqito:
            ans += nalverqito - x + 1
            x *= 1000

        return ans