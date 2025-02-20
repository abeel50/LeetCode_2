class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def backTrack(s):
            if len(s) > len(nums[0]):
                return False
            bstr = "" .join(s)
            if len(s) == len(nums[0]) and bstr not in nums:
                return True
            for c in ['0', '1']:
                s.append(c)
                if backTrack(s):
                    return "".join(s)
                s.pop()
            return False
                    
        return backTrack([]) 
        
