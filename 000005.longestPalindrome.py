class Solution:
    def longestPalindrome(self, s: str):
        if len(s)<2:
            return s
        longest_palindrome_string = s[0]

        for index, start_char in enumerate(s):
            new_string = start_char
            for current_char in s[index+1:]:
                new_string += current_char
                if new_string == new_string[::-1] and len(new_string)>len(longest_palindrome_string):
                    longest_palindrome_string = new_string

        return longest_palindrome_string
    