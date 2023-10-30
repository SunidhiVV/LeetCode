class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                #print(f"{i} {magazine}")
                magazine = magazine.replace(i,"",1)
                #print(f"{i} {magazine}")
        return True


