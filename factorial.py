
class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        dict_pre = []
        for i in nums:
            if target - i in dict_pre:
                dict_pre.append(i)
                ind1 = dict_pre.index(i)
                dict_pre[ind1] = None
                return ind1, dict_pre.index(target - i)
            else:
                dict_pre.append(i)
                    
sl = Solution
print(sl.twoSum([3, 3], 6))