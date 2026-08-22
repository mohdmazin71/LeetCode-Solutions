class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n
        s = 0
        p = 1

        while n:
            digit = n % 10
            s += digit
            p *= digit
            n //= 10

        return original % (s + p) == 0