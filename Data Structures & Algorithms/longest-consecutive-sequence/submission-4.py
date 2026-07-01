class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ordered = sorted(nums)
        tempSeq = 1     #single element is always in order
        longestSeq = 1
        n = len(ordered)
        if n == 0:
            return 0
        for i in range(n - 1):
            #bypass the duplicates
            if ordered[i] == ordered[i+1]:
                continue
            elif ordered[i] + 1 == ordered[i+1]:
                tempSeq += 1
            else:
                longestSeq = max(longestSeq, tempSeq)
                tempSeq = 1
        longestSeq = max(longestSeq, tempSeq)
        return longestSeq
