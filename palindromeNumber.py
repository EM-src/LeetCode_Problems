class Solution(object):
    def isPalindrome(self, x):
        num = []
        for i in str(x):
            num.append(i)
        if num[::] == num[::-1]:
            return True

# Test cases
testCase = Solution()
print(testCase.isPalindrome(121))
print(testCase.isPalindrome(-121))
print(testCase.isPalindrome(10))