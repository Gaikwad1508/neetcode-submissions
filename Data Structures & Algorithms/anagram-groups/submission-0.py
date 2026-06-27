class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in anagramMap:
                anagramMap[sortedWord].append(word)
            else:
                anagramMap[sortedWord] = [word]
        return list(anagramMap.values())