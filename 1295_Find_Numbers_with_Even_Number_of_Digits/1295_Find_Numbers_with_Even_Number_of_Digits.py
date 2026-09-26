nums = [12,345,2,6,7896]


even = 0

for i in range(len(nums)):
    if len(str(nums[i])) % 2 == 0:
        even+=1

print(even) 
    