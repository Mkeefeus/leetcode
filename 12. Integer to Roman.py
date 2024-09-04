# Given an integer, convert it to a Roman numeral.
# I've already done the other way around so this shouldn't be too bad
# I can either convert the int to a string then go char by char, or do some math to isolate digits
# If you wanted to avoid string conversion for some reason, you could reuse these functions from the Palindromic number problem. However, this problem does not say to do so
# def countDigits(self, x: int) -> int:
#     count = 0
#     while x > 0:
#         count = count + 1
#         x = x // 10
#     return count

# def getNthDigit(self, x: int, n: int):
#     divisor = 10 ** (n - 1)

#     digit = (x // divisor) % 10
#     return digit
# if its right on or is a subtractive its easy, need to figure out the logic for the other cases
# This is my first working solution, but I think I can clean it up before submitting.
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         solution = ""
#         subtractives = {
#             "4": "IV",
#             "9": "IX",
#             "40": "XL",
#             "90": "XC",
#             "400": "CD",
#             "900": "CM",
#         }
#         numerals = {
#             "1": "I",
#             "5": "V",
#             "10": "X",
#             "50": "L",
#             "100": "C",
#             "500": "D",
#             "1000": "M",
#         }
#         numStr = str(num)
#         reversedString = numStr[::-1]
#         for i in range(len(reversedString)):
#             digit = reversedString[i]
#             digitAsInt = int(digit)
#             place = pow(10, i)
#             placedDigit = str(digitAsInt * place)
#             if placedDigit in subtractives:
#                 solution = subtractives[placedDigit] + solution
#             elif placedDigit in numerals:
#                 solution = numerals[placedDigit] + solution
#             else:
#                 if int(digit) < 5:
#                     solution = numerals[str(place)] * digitAsInt + solution
#                 else:
#                     prefixNumeral = numerals[str(place * 5)]
#                     numeral = numerals[str(place)]
#                     multiplier = digitAsInt - 5
#                     solution = prefixNumeral + (numeral * multiplier) + solution
#         return solution
# I was able to change the logic to remove the need for the subtractives table
# This solution landed squarely in the middle of the pack. Looking at the better solutions they taking a more mathematical approach
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         solution = ""
#         numerals = {
#             "1": "I",
#             "5": "V",
#             "10": "X",
#             "50": "L",
#             "100": "C",
#             "500": "D",
#             "1000": "M",
#         }
#         numStr = str(num)
#         reversedString = numStr[::-1]
#         for i in range(len(reversedString)):
#             digit = reversedString[i]
#             digitAsInt = int(digit)
#             place = pow(10, i)
#             placedDigit = str(digitAsInt * place)
#             if placedDigit in numerals:
#                 solution = numerals[placedDigit] + solution
#             elif digitAsInt == 4:
#                 solution = numerals[str(place)] + numerals[str(place * 5)] + solution
#             elif digitAsInt == 9:
#                 solution = numerals[str(place)] + numerals[str(place * 10)] + solution
#             elif int(digit) < 5:
#                 solution = numerals[str(place)] * digitAsInt + solution
#             else:
#                 prefixNumeral = numerals[str(place * 5)]
#                 numeral = numerals[str(place)]
#                 multiplier = digitAsInt - 5
#                 solution = prefixNumeral + (numeral * multiplier) + solution
#         return solution
# The way this mathematical approach works is by going down the list of numerals. Subtract 1000 until the number is less then 1000, then move on to 900, etc
# That being said, this performed worse somehow even though its practically the same code as the top answer. I'm convinced you get better scores by being subscribed at this point.
# Still a good exercise none the less, and cleaner code overall.

class Solution:
    def intToRoman(self, num: int) -> str:
        solution = ""
        numerals = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        for subtractor in numerals:
            numeral = numerals[subtractor]
            while subtractor <= num:
                num -= subtractor
                solution += numeral
        return solution

test = Solution()
print(test.intToRoman(3749))
