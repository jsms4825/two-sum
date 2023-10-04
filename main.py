from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    sol = []
    
    for x in nums:
        another = target - x
        if another in nums:
            sol.append(nums.index(another))
            sol.append(nums.index(x))
            break
    return sol
