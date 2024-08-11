/*
Given a string s, return the longest palindromic substring in s.

I think this might have some similar elements to problem 3.

Notably, I need to return the string, not its length this time

I've written what I think is a good function to check if something is a palindrome, so thats a good start.

I could generate every possible substring, then run each through the palindrome, and get the longest

I could generate a map of the string, with the keys being the char and the values being the indices of the char

looking at the hints

Hint 1: How can we reuse a previously computed palindrome to compute a larger palindrome?
    We could check at each end to see if the palindrome continues.
Hint 2: If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
Hint 3: If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. 
Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.

I don't think I will need this checkIfPalindrome function, but I'm gonna save it here anyway

function checkIfPalindrome(s: string): boolean {
    const strLen = s.length;
    const even = strLen % 2 === 0;
    for (let i = 0; i < (even ? strLen / 2 : Math.floor(strLen / 2)); i++) {
        if (s[i] != s[strLen - 1 - i]) {
            return false;
        }
    }
    return true;
}

I have a solution now, it loops through each of the chars in the string, and then checks outward in each direction to find the longest palindrome that it is in the center of.
I've got a gut feeling there is a better way, going to try to think of what it might be.
Going to submit this and see what others did.
First submit has a bug, does not work for condition "aaaa"
I am entirely stuck on this, I cant think of a way that isn't brute forcing checking if the string is all the same char. Going to read the editorial. This is what I got to before

function longestPalindrome(s: string): string {
    let palindrome = s[0];
    let maxLength = 0;
    for (var i = 0; i < s.length; i++) {
        let checkPalindrome = s[i];
        let left = i - 1;
        let right = i + 1;
        while (left >= 0 || right < s.length) {
            const leftChar = left >= 0 ? s[left] : undefined;
            const rightChar = right < s.length ? s[right] : undefined;
            if (!leftChar && !rightChar) break;
            if (leftChar === rightChar) {
                checkPalindrome = `${leftChar}${checkPalindrome}${rightChar}`;
                left--;
                right++;
            } else if (leftChar || rightChar) {
                if (leftChar === s[i]) {
                    checkPalindrome = `${leftChar}${checkPalindrome}`;
                    left--;
                } else if (rightChar === s[i]) {
                    checkPalindrome = `${checkPalindrome}${rightChar}`;
                    right++;
                } else {
                    break;
                }
            } else {
                break;
            }
        }
        if (checkPalindrome.length > maxLength) {
            palindrome = checkPalindrome;
            maxLength = palindrome.length;
        }
    }
    return palindrome;
}

Solution 3 is along the same lines of what I was thinking. Expand out from the center of a potential palindrome.
Their implementation is tracking indices rather then a creating and modifying a string. I think I for some reason assumed using string methods would be slower
Overall, I am happy that my idea of the methodology was correct.
I now understand why I couldn't get the aaaa case. I was so focused on trying to get it to work on the first loop of the forloop, that I forgot it could get it later.
The solution in the editorial would solve that case when i=1
*/


function longestPalindrome(s: string): string {
    function expand(i: number, j: number): string {
        let left: number = i;
        let right: number = j;

        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }

        return s.slice(left + 1, right);
    }

    let ans: string = "";

    for (let i = 0; i < s.length; i++) {
        let odd: string = expand(i, i);
        if (odd.length > ans.length) {
            ans = odd;
        }
        let even: string = expand(i, i + 1);
        if (even.length > ans.length) {
            ans = even;
        }
    }

    return ans;
}

console.log(longestPalindrome("aaaa"));
