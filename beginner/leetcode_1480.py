class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = []
        for i in range(0, len(nums)):
            print(f'i = {i}')
            sum = 0
            for j in range(0, i+1):
                print(f'j = {j}')
                sum += nums[j]
            runningSum.append(sum)
        return runningSum


nums = [1, 1, 1, 1, 1]
test = Solution()
print(test.runningSum(nums=nums))
