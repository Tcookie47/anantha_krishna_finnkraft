def summ(nums, target):
    seen = set()
    for num in nums:
        if target - num in seen:
            return (nums.index(target - num), nums.index(num))
        seen.add(num)
    return None

print(summ([2, 7, 11, 15], 18))