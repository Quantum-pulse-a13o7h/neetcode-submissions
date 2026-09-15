class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for word in strs :
            arr=[0]*26
            for ch in word :
                arr[ord(ch)-ord('a')]+=1
            b = tuple (arr)
            res[b]=res.get(b,[])
            res[b].append(word)
        return list(res.values())
