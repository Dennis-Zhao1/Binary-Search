def binary_search(nums,target):
    if nums == None:
        return -1

    high = len(nums) - 1
    low = 0
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

nums = [i for i in range(10)]
print(binary_search(nums,8))

