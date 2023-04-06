class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        for x in s:
            if x in t:
                t = t.replace(x, '', 1) 
            else:
                return False
        
        if len(t) == 0:
            return True
        return False