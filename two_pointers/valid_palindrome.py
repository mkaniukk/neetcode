class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s = ''.join(ch for ch in s if ch.isalnum()).lower()
        return s == s[::-1]