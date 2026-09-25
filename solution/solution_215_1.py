import random
from random import Random


def findKthLargest(nums, start, end, k):
    if start >= end:
        return nums[start]

    divide = partition(nums, start, end)

    if len(nums) - k < divide:
        return findKthLargest(nums, start, divide - 1, k)
    elif len(nums) - k > divide:
        return findKthLargest(nums, divide + 1, end, k)
    else:
        return nums[divide]

def partition(nums, start, end):
    randint = random.randint(start, end)
    nums[randint], nums[start] = nums[start], nums[randint]

    left = start + 1
    right = end
    while left < right:
        while left < right and nums[left] <= nums[start]:
            left += 1
        while left < right and nums[right] >= nums[start]:
            right -= 1
        if left != right:
            nums[left], nums[right] = nums[right], nums[left]

    if left == right and nums[left] <= nums[start]:
        left += 1
    nums[start], nums[left - 1] = nums[left - 1], nums[start]
    return left - 1

def findKthLargest3P(nums, start, end, k):
    if start >= end:
        return nums[start]

    a, b = partition3ptr(nums, start, end)
    target = len(nums) - k

    if target < a:
        return findKthLargest3P(nums, start, a - 1, k)
    elif target > b:
        return findKthLargest3P(nums, b+1, end, k)
    else:
        return nums[target]

def partition3ptr(nums, start, end):
    randint = random.randint(start, end)
    nums[randint], nums[start] = nums[start], nums[randint]

    left = start
    right = end
    i = start + 1
    while i < right:
        if nums[i] < nums[left]:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        elif nums[i] == nums[left]:
            i += 1
        else:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
    if i == right:
        if nums[i] < nums[left]:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
        elif nums[i] > nums[left]:
            right -= 1
        else:
            i += 1
    return left, i - 1


if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    print(findKthLargest3P(nums, 0, len(nums) - 1, k))

