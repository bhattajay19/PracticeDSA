a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk = 5


def arrChunk(nums, ch):
    n = len(nums)
    temp_res = []
    result = []
    k = 0
    for i in range(n):
        k += 1
        temp_res.append(nums[i])
        if k%ch == 0:
            result.append(temp_res)
            temp_res = []
            k = 0
    if temp_res:
        result.append(temp_res)

    return result


print(arrChunk(a, chunk))