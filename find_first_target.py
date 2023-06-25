nums = [4,5,5,5,5,5,5,6,7,8]
target = 5

nums1 = [5,5,5,5,5,5,6,7,8]
target = 5
# find the first target

def find_first(nums,target):
    left = 0
    right = len(nums) - 1

    while left < right - 1:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1

print(find_first(nums,target))
print(find_first(nums,9))
print(find_first(nums1,target))