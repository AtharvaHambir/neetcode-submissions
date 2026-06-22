class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prev={}

        for i in strs:
            k= "".join(sorted(i))
            if k not in prev:
                prev[k]= []
            prev[k].append(i)
        return list(prev.values())    