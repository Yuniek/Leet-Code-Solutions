"3498. Reverse Degree of a String"
class Solution:
    def reverseDegree(self, s: str) -> int:
        result, idx = 0, 1
        for char in s:
            result += (123-ord(char))*idx
            idx+=1
        return result