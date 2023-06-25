# find the K elements in the array that is closest to the target number
nums = [1,2,3,8,9]
k = 3
target = 4

def find_k(nums,k,target):
    left = 0
    right = len(nums) - 1 
    result = []
    count = 0

    while left < right - 1:
        mid = left + (right - 1)
        if nums[mid] == target:
            result.append(mid)
            count += 1
            left = mid - 1
            right = mid + 1
            break
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    
    while count <= k:
        if(abs(nums[left] - target) <= abs(nums[right] - target) ):
            result.append(left)
            left = left - 1
            count += 1
        else:
            result.append(right)
            right = right + 1
            count += 1
    return result


print(find_k(nums,k,target))



