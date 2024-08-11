# Given an integer x, return true if x is a palindrome, and false otherwise.
# Could you solve it without converting the integer to a string?
#
# In problem 5, I made this function to check if a string was a palindrome
# function checkIfPalindrome(s: string): boolean {
#     const strLen = s.length;
#     const even = strLen % 2 === 0;
#     for (let i = 0; i < (even ? strLen / 2 : Math.floor(strLen / 2)); i++) {
#         if (s[i] != s[strLen - 1 - i]) {
#             return false;
#         }
#     }
#     return true;
# }
# Converting that to python, the solution looks like this
#
# class Solution:
#     def checkIfStringIsPalindrome(self, s: str) -> bool:
#         stringLength: int = len(s)
#         isEvenLen = (stringLength % 2 == 0)
#         forRange = int(stringLength /  2) if isEvenLen else stringLength // 2
#         for x in range(forRange):
#             if s[x] != s[stringLength - 1 - x] :
#                 return False
#         return True
#     def isPalindrome(self, x: int) -> bool:
#         xAsString = str(x)
#         return self.checkIfStringIsPalindrome(xAsString)
#
# However, the problem also challenges us to try to do it without converting to a string, so lets try that.
# We will need to know the number of digits in the int, and maybe if that number is odd or even
# then we need to isolate two digits at a time from the end and the start, and see if they are the same
# Had to do some googling for this one. I knew the methodology was right, but was having trouble with the math used to isoloate the digits.
# All of the top leetcode solutions for python are converting it to a string lol. That seems to be much faster. 
# Today I learned python can reverse strings like string[::-1]


class Solution:
    def countDigits(self, x: int) -> int:
        count = 0
        while x > 0:
            count = count + 1
            x = x // 10
        return count

    def getNthDigit(self, x: int, n: int):
        divisor = 10 ** (n - 1)

        digit = (x // divisor) % 10

        return digit

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digitCount = self.countDigits(x)
        evenDigitCount = digitCount % 2 == 0
        forRange = int(digitCount / 2) if evenDigitCount else digitCount // 2
        for y in range(forRange):
            higherPlace = self.getNthDigit(x, digitCount - y)
            lowerPlace = self.getNthDigit(x, y + 1)
            if higherPlace != lowerPlace:
                return False
        return True


solution = Solution()

print(solution.isPalindrome(1000110001))
