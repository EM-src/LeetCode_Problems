class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
    
# Test Cases
haystack = "sadbutsad"
needle = "sad"
# haystack = "leetcode"
# needle = "leeto"
testCase = Solution()
print(testCase.strStr(haystack, needle))