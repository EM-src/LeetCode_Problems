class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(0, n-1):
            for j in range(i+1, n):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

# Test Cases:
testCase = Solution()
print(testCase.twoSum([2,7,11,15], 9))
print(testCase.twoSum([3,2,4], 6))
print(testCase.twoSum([3,3], 6))