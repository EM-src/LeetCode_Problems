class Solution(object):
  def isValid(self, s):
        sLength = len(s)
        # Create a stack
        stack = []
        for idx in range(0, sLength):
            # Only pop out the elements from stack if stack is not empty and
            # Only pop out the elements if current value is closing bracket and 
            # stack top is opening bracket corresponding to same closing bracket
            if len(stack) > 0 and ((s[idx] == ')' and stack[-1] == '(') or (s[idx] == '}' and stack[-1] == '{') or (s[idx] == ']' and stack[-1] == '[')):
                stack.pop()
            # Else add element at the top of stack
            else:
                stack.append(s[idx])
        # If stack is empty meaning it is valid else it is not valid
        return len(stack) == 0

# Test cases
testCase = Solution()
print(testCase.isValid("()"))
print(testCase.isValid("()[]{}"))
print(testCase.isValid("(]"))
print(testCase.isValid("([)]"))