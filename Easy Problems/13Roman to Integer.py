"""
[Problem description] EASY
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

来源：力扣（LeetCode）
"""
# updated by: Tao 2020
########################################################################################################################
"""
【知识点总结】：
1.count = str.count(str1) # 计算字符串中另一字符串出现的次数
2.str = str.replace(str1,'')  # 删除字符串中的另一字符串（利用为空字符的方式）
3.list.extend(list1) # 将list1合并至list，直接修改list，无返回
"""
########################
"""
【思路】：从输入字符串中计算出每个规定字符（串）的个数，然后乘以对应数值相加即可，注意要首先
          提取出特殊字符串
"""
class Solution:
    def romanToInt(self, s):
        r2I_dict = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40,'L':50,\
                    'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        roman_special = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        roman_normal = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        roman = []
        roman.extend(roman_special)     # 特殊字符串要首先提取出
        roman.extend(roman_normal)

        output = 0
        for i in range(len(roman)):
            count = s.count(roman[i])
            output += count*r2I_dict[roman[i]]
            s = s.replace(roman[i],'')  # 提取出字符串后则删除，以免后续重复提取
        return output

########################################################################################################################
if __name__ == "__main__":
    s = 'MCMXCIV'

    test = Solution()
    output = test.romanToInt(s)
    print(output)
