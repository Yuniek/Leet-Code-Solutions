"8. String to Integer (atoi)"
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        number = 0

        def ret(num):
            if MIN_NUM < num and num < MAX_NUM:
                return num
            else:
                return MIN_NUM if num < 0 else MAX_NUM

        MIN_NUM = -2147483648
        MAX_NUM = 2147483647

        digits = {str(i) for i in range(10)}
        special_chars = {' ', '\t', '+', '-'}

        allowed_char = digits | special_chars

        for current_char in s:
            if current_char in allowed_char:
                if current_char in ('+','-'):
                    sign = 1 if current_char == '+' else -1
                    allowed_char = digits
                elif current_char in digits:
                    number *= 10
                    number += int(current_char)
                    allowed_char = digits
            else:
                return ret(number*sign)

        return ret(number*sign)