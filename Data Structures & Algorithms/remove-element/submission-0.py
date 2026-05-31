class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swapPos = len(nums) - 1

        for index in range(len(nums) - 1, -1, -1):
            if nums[index] == val:
                old = nums[swapPos]
                nums[swapPos] = nums[index]
                nums[index] = old
                swapPos -= 1

        return swapPos + 1