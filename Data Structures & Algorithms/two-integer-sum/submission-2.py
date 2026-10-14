class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums=[1, 2, 4, 5, 7], target=6 
        diff = {};
        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in diff: 
                return [diff[compliment], i]

            diff[nums[i]] = i