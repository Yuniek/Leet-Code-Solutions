"10. Regular Expression Matching"
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        res = re.search(p,s)

        if not res:
            return False

        return res.group()==s