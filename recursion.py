def binary_search(nums,target):
    if nums == None:
        return -1

    high = len(nums) - 1
    low = 0
    mid = low + (high - low) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(nums[mid+1:],target)
    else:
        return binary_search(nums[:mid],target)

nums = [i for i in range(10)]
print(binary_search(nums,11))