def removeDuplicates(nums):
    if not nums:
        return 0

    write = 1  # position to write next unique element

    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1

    return write


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = removeDuplicates(nums)

print(k)  # 5
print(nums)