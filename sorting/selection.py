# nums = [9, 8, 6, 7, 6, 5, 4, 3, 2]

nums = [3, 2, 1, 7, 6, 5, 4, 3, 2]

n = len(nums)


for i in range(0, n):
    min_index= i
    for j in range (i+1 , n):
        if nums[j]<nums[min_index]:
            min_index =j

        nums[i], nums[min_index] = nums[min_index], nums[i]

print(nums)