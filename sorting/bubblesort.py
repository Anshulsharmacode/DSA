nums = [9, 8, 6, 7, 6, 5, 4, 3, 2]
l = len(nums)

for i in range(l-2, -1,-1):
    for j in range(0 , i+1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]    
print(nums)