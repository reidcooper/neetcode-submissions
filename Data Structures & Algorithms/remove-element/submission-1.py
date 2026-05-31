class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swapPos = len(nums) - 1

        for index in reversed(range(len(nums))):
            if nums[index] == val:
                nums[swapPos], nums[index] = nums[index], nums[swapPos]
                swapPos -= 1

        return swapPos + 1