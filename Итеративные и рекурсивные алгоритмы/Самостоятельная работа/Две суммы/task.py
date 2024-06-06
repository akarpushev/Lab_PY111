from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    for idx1, value1 in enumerate(nums):
        for idx2, value2 in enumerate(nums):
            if value1 + value2 == target and idx1 != idx2:
                return [idx1, idx2]






