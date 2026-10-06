class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #We will implement a hashmap with the key being the integers and the vale being the frequency
        freq_hashmap = {}
        for i in nums:
            if i in freq_hashmap:
                freq_hashmap[i] += 1; 
            else: 
                freq_hashmap[i] = 1; #init if int isnt in hashmap 
        for i in freq_hashmap:
            if freq_hashmap[i] > 1: 
                return True; 
        return False; 
