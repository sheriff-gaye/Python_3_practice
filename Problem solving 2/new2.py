def solve(nums):
   nums.sort(key=lambda num: (bin(num).count("1"), num))
   return nums

nums = [1,3]
print(solve(nums))