class Solution:
    def isValid(self, ch: chr) -> bool:
        return (ord('a') <= ord(ch) <= ord('z') or
            ord('A') <= ord(ch) <= ord('Z') or
            ord('0') <= ord(ch) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        stripped = ''.join([ch.lower() for ch in s if self.isValid(ch)])
        print(stripped)
        return (stripped[::-1]) == stripped