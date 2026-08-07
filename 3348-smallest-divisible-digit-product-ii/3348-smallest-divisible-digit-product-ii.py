import math

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Validate prime factors of t
        temp_t = t
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                temp_t //= p
        if temp_t > 1:
            return "-1"
        
        n = len(num)
        
        # Helper function to find the minimum required digits to satisfy a target t
        def get_min_digits_needed(target: int) -> list:
            # We want to satisfy target with the largest single digits (9, 8, 7, 6, 5, 4, 3, 2)
            # to minimize the total count of digits needed.
            digits = []
            for d in [9, 8, 7, 6, 5, 4, 3, 2]:
                while target % d == 0:
                    digits.append(d)
                    target //= d
            # If target can't be reduced to 1 using 2..9, it's impossible
            if target > 1:
                return None
            return sorted(digits)

        # Prefix products tracking (ignoring 0s, but we track the first 0 if present)
        # prefix_t[i] represents the required remaining 't' factor after first i digits
        prefix_t = [1] * (n + 1)
        prefix_t[0] = t
        
        first_zero = -1
        for i in range(n):
            if num[i] == '0':
                first_zero = i
                break
            # Compute remaining t needed
            d = int(num[i])
            g = math.gcd(prefix_t[i], d)
            prefix_t[i + 1] = prefix_t[i] // g

        # Case 1: The number itself is zero-free and already satisfies t
        if first_zero == -1 and prefix_t[n] == 1:
            return num

        # Case 2: Try to find a prefix match and increment the next digit
        # If there's a zero, we cannot match past the zero position.
        limit = n - 1 if first_zero == -1 else first_zero
        
        for i in range(limit, -1, -1):
            curr_t = prefix_t[i]
            start_digit = int(num[i]) + 1
            
            for d in range(start_digit, 10):
                rem_t = curr_t // math.gcd(curr_t, d)
                req_digits = get_min_digits_needed(rem_t)
                
                if req_digits is not None:
                    rem_len = n - 1 - i
                    if len(req_digits) <= rem_len:
                        # Construct the optimal suffix
                        # Fill the leading available spaces with '1's, then place req_digits
                        ones_count = rem_len - len(req_digits)
                        suffix = ['1'] * ones_count + [str(x) for x in req_digits]
                        return num[:i] + str(d) + "".join(suffix)
                        
        # Case 3: We need to increase the length of the number
        # Find the smallest combination of digits that satisfies t
        req_digits = get_min_digits_needed(t)
        total_needed_len = max(n + 1, len(req_digits))
        
        ones_count = total_needed_len - len(req_digits)
        return '1' * ones_count + "".join(str(x) for x in req_digits)

