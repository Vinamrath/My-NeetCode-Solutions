class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters and make lowercase
        c = ''.join(char.lower() for char in s if char.isalnum())
        
        a = 0
        b = len(c) - 1

        while a < b:
            if c[a] != c[b]:
                return False
            a += 1
            b -= 1

        return True