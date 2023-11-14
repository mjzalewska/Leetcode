def twoSum(nums: list[int], target: int)-> list[int]:
    solution = []
    if len(nums) < 2:
                return []
    elif len(nums) == 2:
                solution.extend([0, 1])
    else:
            for i in range(len(nums)):
                for j in range(i, len(nums)):
                    if nums[i] + nums[j] == target and  i != j:
                        solution.extend([i, j])
    return solution

print(twoSum([3, 3], 6))
print(twoSum([1,2,3,4], 6))

