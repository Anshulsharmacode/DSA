nums = [1,2,3,4,5,7,8,9,4,1,2,3,5,4,75]

result = dict()

# for i in range (1, len(nums)):
#     if nums[i] in result:
#         result[nums[i]]+=1
#     else:
#         result[nums[i]]=1

# print(result)

##meethod 2 

for i in range (0 ,len(nums)):
    result [nums[i]]= result.get(nums[i],0)+1

print(result)