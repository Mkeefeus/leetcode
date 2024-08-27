# Given a roman numeral, convert it to an integer.
# Here is what I am thinking
# Loop through the string, if character[i] exists in subtractions, check the next character and increment by 1, otherwise continue
# This passed, however we can remove the subtractions dict, and instead check if the value of char is less then the value of nextChar
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         numeralDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         subtractions = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}
#         integer = 0
#         skip = False
#         for index, char in enumerate(s):
#             if skip:
#                 skip = False
#                 continue
#             if (
#                 char in subtractions
#                 and index < len(s) - 1
#                 and s[index + 1] in subtractions[char]
#             ):
#                 nextChar = s[index + 1]
#                 skip = True
#                 integer += numeralDict[nextChar] - numeralDict[char]
#                 continue
#             integer += numeralDict[char]

#         return integer


class Solution:
    def romanToInt(self, s: str) -> int:
        numeralDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        length = len(s)
        for index in range(length):
            if index + 1 < length and numeralDict[s[index]] < numeralDict[s[index + 1]]:
                result -= numeralDict[s[index]]
            else:
                result += numeralDict[s[index]]
        return result


mySolution = Solution()
print(mySolution.romanToInt("MCMXCIV"))
