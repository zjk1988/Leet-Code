方法1，遍历一遍字符串把符合要求的字符加入到新开的列表中，最后判断这个列表是否是可反转的，时间复杂度和空间复杂度分数都不高
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = []
        for i in s:
            if  i.isdigit():
                ss.append(i)
            elif i.isalpha():
                ss.append(i.lower())
        re = ''.join(ss)
        print(re)
        if re == re[::-1]:
            return True 
        else:
            return False

方法2：双指针法
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        r = len(s)-1
        l = 0
        while l<r:
            #不是字母和数字就各自往前走
            if not s[l].isalnum():
                l = l+1
                continue
            if not s[r].isalnum():
                r = r-1
                continue
            
            #是，需要判断同否
            if s[r].lower() == s[l].lower():
                l = l+1
                r = r-1
            else:
                return False
        return True
            