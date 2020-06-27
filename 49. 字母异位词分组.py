维护一个字典，key是串的sorted（），value是各个串sorted值等于key的原来形式
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())