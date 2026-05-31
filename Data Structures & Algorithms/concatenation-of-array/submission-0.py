class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Attempt 1
        newArr = []

        for i in range(2):
            for n in nums:
                newArr.append(n)
        
        return newArr

        # Attempt 2 (answer from ex. solutions)
        # n = len(nums)
        # ans = [0] * (2 * n)

        # for i, num in enumerate(nums):
        #     ans[i] = ans[i + n] = num
        
        # return ans