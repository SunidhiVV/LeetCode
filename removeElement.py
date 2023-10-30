class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        for i in nums:
            if i != val:
                nums[p]=i
                p+=1
        return p


