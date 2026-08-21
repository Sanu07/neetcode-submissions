class Solution:

    def _swap(self, nums: List[int], i: int, j: int) -> None:
        tmp: int = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def removeElement(self, nums: List[int], val: int) -> int:
        
        left: int = 0
        right: int = len(nums) - 1
        count: int = 0

        while (left <= right):
            while (left < len(nums) and nums[left] != val):
                left += 1
            while (right >= 0 and nums[right] == val):
                right -= 1
                count += 1
            
            if (left < right):
                self._swap(nums, left, right)
                left += 1
                right -= 1
                count += 1
        return len(nums) - count
        