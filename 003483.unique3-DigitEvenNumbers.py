"3483. Unique 3-Digit Even Numbers"
from typing import List
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        if 0 not in [i%2 for i in digits]:
            return 0

        possible_digits = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i!=j and i!=k and j!=k:
                        if digits[i] != 0 and digits[k]%2==0:
                            possible_digits.add(f"{digits[i]}{digits[j]}{digits[k]}")
        return len(possible_digits)