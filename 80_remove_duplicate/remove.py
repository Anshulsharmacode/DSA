nums = [1,1,1,2,2,3]

i=0
j=1

while j < len(nums):
    if nums[i] == nums[j]:
        nums.pop(j)
    else:
        j+=1
        i+=1

print(nums)    
