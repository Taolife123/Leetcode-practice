"""
[Problem description] EASY
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.

来源：力扣（LeetCode）
"""
# updated by: Tao 2020
########################################################################################################################
########################
"""
【思路】将输入的整数转换为字符串再转换为列表，即可利用列表的reverse函数进行反转，再转换回整数
【注】Python储数字理论上是无限长度，因此每次计算完后判断大小关系即可
"""
class Solution:
    def reverseInteger(self, x):
        flag_sign = 0   # 为负数则置1,否则为0
        if x<0:
            flag_sign = 1
        x_list = list(str(abs(x)))  # 此处先将绝对值整数转换为字符串再转换为列表，注意：单个整数不可直接进行列表反转
        x_list.reverse()    # 进行列表反转
        if flag_sign == 1:
            output = int(''.join(x_list))*-1    # 此处注意将列表转换为字符串的方式
        else:
            output = int(''.join(x_list))
        if output>=-2**31 and output<=2**31-1:  # 此处注意32位整数的范围[-2^31, 2^31-1]
            return output
        else:
            return 0



########################################################################################################################
if __name__ == "__main__":
    x = 153423123123

    test = Solution()
    output = test.reverseInteger(x)
    print(output)

