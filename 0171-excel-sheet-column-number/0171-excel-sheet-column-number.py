class Solution:
    def titleToNumber(self, columnTitle):
        result = 0
        for ch in columnTitle:
            value = ord(ch) - ord('A') + 1
            result = result * 26
            result = result + value
        return result