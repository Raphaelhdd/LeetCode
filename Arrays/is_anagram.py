# Trivial solution : count the number of occurence of each letter anc check if match 
#Running Time: O(n + m)
#Space complexity : O(n+m) because at most 26 letters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        occurences_s = dict()
        occurence_t = dict()
        for index in range(len(s)):
            occurences_s[s[index]] = 1 + occurences_s.get(s[index],0)
            occurence_t[t[index]] = 1 + occurence_t.get(t[index],0)
        return occurence_t == occurences_s
        
#We can simply sorted and check if the same
#Here advantage, space complexity O(1)
#Time complexity : O(nlogn + mlogm)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    
#Interesting solution
#We create a list of 26 and we will add 1 in the place of the letter we saw in s and remove occurence of t and we need to have an array of 0
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_table = [0] * 26
        for i in range(len(s)):
            hash_table[ord(s[i]) - ord('a')] += 1
            hash_table[ord(s[i]) - ord('a')] -= 1
        for value in hash:
            if value != 0:
                return False
        return True