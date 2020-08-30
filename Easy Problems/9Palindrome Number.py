"""
[Problem description] EASY
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?

来源：力扣（LeetCode）
"""
# updated by: Tao 2020
########################################################################################################################
########################
"""
【注】注意（1）list.reverse()的用法（无返回值，直接修改原列表）
          （2）列表反转后得到的是单个的字符构成的列表，还需要使用''.joint()整合成字符串
"""
class Solution:
    def isPalindrome(self, x):
        x_str = str(x)
        x_list = list(x_str)
        x_list.reverse()
        x_str_reverse = ''.join(x_list)
        if x_str_reverse == x_str:
            return True
        else:
            return False

########################################################################################################################
if __name__ == "__main__":
    x = -121

    test = Solution()
    outpot = test.isPalindrome(x)
    print(outpot)

