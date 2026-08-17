class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_index: dict = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in number_index:
                return [number_index.get(target - nums[i]), i]
            number_index[nums[i]] = i