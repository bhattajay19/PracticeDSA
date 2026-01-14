from sys import hash_info


def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        length = min(height[left], height[right])
        area = width * length
        max_area = max(max_area, area)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))