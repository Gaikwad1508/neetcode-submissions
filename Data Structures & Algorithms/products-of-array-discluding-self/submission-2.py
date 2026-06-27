class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #using prefix cumulative product and postfix cumulative product
        n = len(nums)
        ans = [1] * n
        
        #for prefix cumulative product(left to right)
        prefix = 1                  #product
        for i in range(n):          #traverse from first index towards right
            ans[i] = prefix         #first filling 0 index with 1 then in second iteration 1st index fill with left side numbers except current to current index of ans
            prefix *= nums[i]       #updates prefix for next index value by cumulative multiplication

        #for postfix cumulative product(right to left)
        postfix = 1
        for i in range(n-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans



        #Brute force O(N^2)
        '''
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
        '''
