class Solution:
    def trap(self, height: list[int]) -> int:
        return trap(height)

def trap(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total = 0

    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
        if left_max < right_max:
            total += left_max - height[left]
            left += 1
        else:
            total += right_max - height[right]
            right -= 1
    return total