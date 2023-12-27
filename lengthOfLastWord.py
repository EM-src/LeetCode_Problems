class Solution(object):
    def lengthOfLastWord(self, s):
      strippedStr = s.rstrip()
      idx = len(strippedStr)-1
      lword = []
      if len(strippedStr) > 1:
        while s[idx] != " " and idx >= 0:
            lword.append(strippedStr[idx])
            idx -= 1
        return len(lword)
      return len(strippedStr)
    
# Test Cases
# s = "Hello World"
# s = "a"
s = "   fly me   to   the moon  "
testCase = Solution()
print(testCase.lengthOfLastWord(s))
