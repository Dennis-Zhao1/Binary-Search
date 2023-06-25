nums = [1,2,3,8,9]
target = 4

def closest(nums,target):
    left = 0
    right = nums[len(nums)-1]

    while left < right - 1:
        mid = left + (right - left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    if abs(nums[left] - target) <= abs(nums[right] - target):
        return left
    else:
        return right

print(closest(nums,target))