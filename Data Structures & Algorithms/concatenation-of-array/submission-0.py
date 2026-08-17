class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res: List[int] = [0] * (2 *len(nums))
        for i in range(len(res)):
            res[i] = nums[i % len(nums)]
        return res