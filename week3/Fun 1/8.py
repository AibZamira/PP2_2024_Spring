def spy_game(nums):
    new_nums = []
    for i in nums:
        if i == 0 or i == 7:
            new_nums.append(i)

    for i in range(len(new_nums) - 2):
        if new_nums[i] == 0 and new_nums[i + 1] == 0 and new_nums[i + 2] == 7:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
