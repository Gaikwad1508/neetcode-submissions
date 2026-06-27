class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)
        
        sorted_keys = sorted(count_map.keys(), key=count_map.get, reverse=True)
        
        return sorted_keys[:k]
        