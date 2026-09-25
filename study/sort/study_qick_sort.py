def quick_sort(nums, start, end):
    if start >= end:
        return
    middle = partition(nums, start, end)
    quick_sort(nums, start, middle - 1)
    quick_sort(nums, middle + 1, end)

def partition(nums, start, end):
    pivot = nums[start]
    left = start + 1
    right = end - 1
    while left < right:
        while left < right and nums[left] <= pivot:
            left += 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        


