class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            index = l + ((r - l) // 2)
            if nums[index] == target:
                return index
            elif nums[index] > target:
                r = index - 1
            elif nums[index] < target:
                l = index + 1

        return -1
