#BEST SOLUTION
# WE have 26 letters at all
# we will have an array called count
# For each word we will have his count
# We have a dict with key the count and the value is the list of words
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(word) #LIST NOT KEYS
        return list(res.values())
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            res[sorted_word].append(word)
        return list(res.values())


#My solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_words_anagram = dict()
        final_lst = []
        for index, word in enumerate(strs):
            word = ''.join(sorted(word))
            if word in dict_words_anagram:
                dict_words_anagram[word].append(init_word)
            else:
               dict_words_anagram[word] = [init_word]
        for word in dict_words_anagram:
            final_lst.append(dict_words_anagram[word])    
        return final_lst
        
        
