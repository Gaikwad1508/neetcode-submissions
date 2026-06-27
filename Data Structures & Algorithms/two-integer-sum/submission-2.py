class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[num] = i




        '''
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                else:
                    if (nums[i] + nums[j]) == target:
                        return [i, j]
        '''