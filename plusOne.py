class Solution(object):
    def plusOne(self, digits):
        # Convert the integers in the digits list to strings. Then join them together in one string, cast to an integer and add 1
        onePlus = int("".join(map(str, digits))) + 1
        # Convert the number in above step to string and then convert each character (number) to integer. Then transfrom this to a list
        return list(map(int, str(onePlus)))
    
# Test Cases
digits = [9,9]
# digits = [1,2,3]
# digits = [4,3,2,1]
testCase = Solution()
print(testCase.plusOne(digits))