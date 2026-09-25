class Solution:
    def trap(self, height: list[int]) -> int:
        return trap(height)

def trap(height: list[int]) -> int:
    left_max, right_max = [0] * len(height), [0] * len(height)
    left_max[0] = height[0]
    right_max[len(height) - 1] = height[len(height) - 1]

    for i in range(1, len(height)):
        left_max[i] = max(left_max[i-1], height[i])
        right_max[len(height) - i - 1] = max(right_max[len(height) - i], height[len(height) - i - 1])


    total = sum(max(min(left_max[i-1], right_max[i+1]) - height[i], 0) for i in range(1, len(height) - 1))
    return total
