class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_list = nums
        my_set = set(nums)

        if len(my_list) > len(my_set):
            return True
        return False