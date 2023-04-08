class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        queue = []
        for parenth in s:
            if parenth in opening:
                queue.append(parenth)
            else:
                if not queue or queue.pop() != opening[(closing.index(parenth))]:
                    return False

        if queue:
            return False
        return True


solution = Solution()
print(solution.isValid("((())"))
