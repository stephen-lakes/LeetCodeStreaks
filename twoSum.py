class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        
        for i in range(len(nums)):
            item = nums[i]
            complement = target - item
            if complement not in hashmap.keys():
                hashmap[item] = i
            else:
                return (i, hashmap[complement])
