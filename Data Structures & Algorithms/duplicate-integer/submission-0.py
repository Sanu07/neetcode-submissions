class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res: set() = set()
        for num in nums:
            if num in res:
                return True
            res.add(num)
        return False