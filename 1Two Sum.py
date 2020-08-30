"""
Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

来源：力扣（LeetCode）
"""
# updated by: Tao 2020
########################################################################################################################
########################
"""
方法一：暴力求解法
    时间复杂度：O(n)，空间复杂度：O(1)
    该方法为思路最简单且易懂的方法
    【注】使用list相关函数比直接编写循环运行更快。该方法用in判断替代循环判断，比直接写循环判断更快
"""
class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        output = []
        for i in range(length): # 只使用1次循环
            if (target-nums[i]) in nums:    # 【注】此处用in判断替代循环判断，可提升运算速度
                j = nums.index(target-nums[i])
                if j != i:  # you may not use the same element twice
                    output = [i, j]
                    return output   # return the indices of the two numbers
        return output   # 如果不存在则返回空list
########################
"""
方法二：借助哈希表思想
    时间复杂度：O(n)，空间复杂度：O(n)
    该方法实质上利用python的字典来模拟哈希表查询过程
    【注】哈希表的思路在python中对应字典查询（直接将值和index对应起来，无需循环查找），通过字典查询，可大幅提高查找效率
          in判断和循环判断都相当于进行遍历搜索，而字典查找是直接键值对应，运算效率更高
"""
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):  # enumerate函数得到的两个参数按顺序分别为index和value
            hashmap[num] = index  # 注意：dict[键]=值，即{键：值}
        for i in range(len(nums)):
            j = hashmap.get(target-nums[i]) # 【注】此处用字典查询替代前面in判断或循环判断，可大幅提高查找效率
            if j is not None and j != i:    # you may not use the same element twice
                output = [i, j]
                return output  # return the indices of the two numbers
        return output  # 如果不存在则返回空list


########################################################################################################################
if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    test = Solution()
    output = test.twoSum(nums, target)
    print(output)
