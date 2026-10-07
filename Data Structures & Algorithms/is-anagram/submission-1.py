

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False; 
        s_hashmap = Counter(s); 
        t_hashmap = Counter(t); 
        for i in s_hashmap: 
            if s_hashmap[i] != t_hashmap[i]:
                return False;
        return True; 