class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        tmp = dict()
        for index, value in enumerate(nums):
            if target - value in tmp:
                return [tmp[target - value], index]
            tmp[value] = index
        return []