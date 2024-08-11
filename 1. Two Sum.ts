function twoSum(nums: number[], target: number): number[] {
    const hash: { [key: number]: number } = {};

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        
        if (hash.hasOwnProperty(complement)) {
            return [hash[complement], i];
        }
        
        hash[nums[i]] = i;
    }

    return [];
}