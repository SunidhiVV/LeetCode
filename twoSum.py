class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictnums = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in dictnums:
                return [dictnums[diff], i]
            dictnums[num] = i
            


