class Solution(object):
  def searchInsert(self, nums, target):
      for idx in range(0, len(nums)):
          if target == nums[idx] or target <= nums[idx]:
              return idx
      return len(nums)


# Test Cases
nums = [1,3,5,6]
target = 5
# target = 2
# target = 7
test = Solution()
print(test.searchInsert(nums, target))
