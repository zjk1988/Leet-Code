方法1：
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
方法2：
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import collections
        return collections.Counter(s) == collections.Counter(t)