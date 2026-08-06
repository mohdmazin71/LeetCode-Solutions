class Solution:
    def smallestNumber(self,n ,t):
        while True:
            product = 1
            x = n
            while x > 0:
                product = product * (x % 10)
                x = x // 10
            if product % t == 0:
                return n
            n += 1