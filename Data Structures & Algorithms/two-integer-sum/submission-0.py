class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i , j in enumerate (nums ):
            need = target - j 
            if need in n :
                return [n[need], i ]
            else :
                n[j]= i 