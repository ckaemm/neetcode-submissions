class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        gorduklerim = {}                    # sayı → index
        for i in range(len(nums)):
            es = target - nums[i]
            if es in gorduklerim:
                return [gorduklerim[es], i]
            gorduklerim[nums[i]] = i