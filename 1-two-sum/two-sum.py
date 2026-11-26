class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}

        for index, value in enumerate(nums):
            need = target - value
            if need in seen:
                return [seen[need],index]
            seen[value]=index
        return []
        