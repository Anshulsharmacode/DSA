nums = [1,2,3,1]
k = 0

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]==nums[j]:
            if abs(i - j) <= k:
                print(True)
            break