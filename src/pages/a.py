from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_values = []
        for num in nums:
            digits = [int(digit) for digit in str(num)]  # 将字符串数字转换为整数
            min_values.append(sum(digits))
        return min(min_values)  # 返回最小值


nums = [999, 19, 199]
print(Solution().minElement(nums))  # 1
