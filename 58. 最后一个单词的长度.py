class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        last = s.split()
        return len(last[-1]) if last else 0