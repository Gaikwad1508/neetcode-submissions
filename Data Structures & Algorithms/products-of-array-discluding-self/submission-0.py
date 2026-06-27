class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        upIndex = 0
        n = len(nums)
        for j in range(n):
            prod = 1
            for i in range(n):
                if i == upIndex:
                    continue
                prod *= nums[i]
            ans.append(prod)
            upIndex += 1
        return ans

