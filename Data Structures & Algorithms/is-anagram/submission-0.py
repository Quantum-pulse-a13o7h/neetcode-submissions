class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr= [0] * 26
        if len (s) != len (t):
            return False
        for ch in s :
            arr[ord(ch)- ord('a')] += 1
        for ch in t :
            arr [ord (ch) - ord('a')] -= 1
        for i in arr :
            if i !=0:
                return False 
        return True 