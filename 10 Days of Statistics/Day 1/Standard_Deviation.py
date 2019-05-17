n = int(input())
nums = [int(x) for x in input().strip().split()]
print(round((sum([(x-(sum(nums) / n))**2 for x in nums])/n)**.5, 1))
