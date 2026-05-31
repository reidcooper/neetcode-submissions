class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = {}
        tally = 1
        prev = None

        for i in range(len(nums)):
            current = nums[i]

            if current == prev:
                tally += 1
            else:
                tally = 1

            maxx[current] = max(tally, maxx.get(current, 1))
            prev = current
        
        return maxx.get(1, 0)