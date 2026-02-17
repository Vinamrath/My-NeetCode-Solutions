class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = [ch.lower() for ch in s if ch.isalnum()]
        a = 0
        b = len(c) - 1
        while a <= b:
                if c[a] == c[b]:
                    a += 1
                    b -= 1
                else:
                    return False
        return True