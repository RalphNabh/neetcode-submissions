class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []

        for char in s: 
            if char.isalnum():
                stack.append(char.lower())
        return stack == stack[::-1]