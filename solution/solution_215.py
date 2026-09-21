def findKthLargest(nums, start, end, k):
    if start >= end:
        return nums[start]

    divide = partition(nums, start, end)
    if len(nums) - k > divide:
        return findKthLargest(nums, divide+1, end, k)
    elif len(nums) - k < divide:
        return findKthLargest(nums, start, divide - 1, k)
    else:
        return nums[divide]

def partition(nums, start, end):
    index = start + 1
    for i in range(start + 1, end + 1):
        if nums[i] <= nums[start]:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
    nums[start], nums[index - 1] = nums[index - 1], nums[start]
    return index - 1

if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    print(findKthLargest(nums, 0, len(nums)-1, k))