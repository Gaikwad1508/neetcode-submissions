class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))




        # my_list = nums
        # my_set = set(nums)

        # if len(my_list) > len(my_set):
        #     return True
        # return False