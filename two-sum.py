def twoSum(nums: list[int], target: int)-> list[int]:
    solution = []
    for i in nums:
        for j in nums[nums.index(i):]:
            if nums.index(i)!=nums.index(j) and (i + j == target):
                solution.extend([nums.index(i),nums.index(j)])
    return solution

print(twoSum([1,2,3,4], 6))
