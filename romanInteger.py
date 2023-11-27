class Solution(object):
    def romanToInt(self, s):
      x = 0
      s_list = []
      for i in s:
        s_list.append(i)
      
      roman_nums_dict = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC':90,
        'C': 100,
        'CD':400,
        'D': 500,
        'CM': 900,
        'M': 1000
      }


      i = 0
      while i <= len(s_list) -1:
        if (i+1) <= len(s_list) - 1 and s_list[i] + s_list[i+1] in roman_nums_dict:
          sub = s_list[i] + s_list[i+1]
          x += roman_nums_dict[sub]
          i +=2
        else:
          x += roman_nums_dict[s_list[i]]
          i +=1        
        
      return x
    
# Test Cases
testCase = Solution()
print(testCase.romanToInt("III"))
print(testCase.romanToInt("LVIII"))
print(testCase.romanToInt("MCMXCIV"))