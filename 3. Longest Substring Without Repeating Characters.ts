/*
First try, very inefficient do to long loop.

function lengthOfLongestSubstring(s: string): number {
    let currMax = 0;
    let bestMax = 0;
    let substringHash: { [key: string]: number } = {};
    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        if (substringHash[char] || substringHash[char] === 0) {
            bestMax = currMax > bestMax ? currMax : bestMax;
            i = substringHash[char]
            substringHash = {}
            currMax = 0
        } else {
            substringHash[char] = i;
            currMax++;
        }
    }
    return currMax > bestMax ? currMax : bestMax;
}

For second attempt, use a left and right variable to track the current substring. When a collision is found, move the left pointer to the position on the first instance of the char + 1

*/

function lengthOfLongestSubstring(s: string): number {
    let left = 0;
    let max = 0;
    let foundChars = new Map<string, number>();
    for (let right = 0; right < s.length; right++) {
        const char = s[right];
        const prevSeen = foundChars.get(char) as number
        if (prevSeen >= left) {
            left = (prevSeen as number) + 1;
        }
        foundChars.set(char, right);
        max = Math.max(max, right - left + 1);
    }
    return max;
}