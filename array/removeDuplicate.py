nums = [1,1,2,2,2,3,3,4,5,6,6,7,8,10]
n = len(nums)

i = 0
j = i+1
while j<n:
    if nums[j]!= nums[i]:
        i+=1
        nums[i],nums[j]= nums[j], nums[i]
    j+=1

print(nums)
print(i+1)
# dic = {}

# for i in range(0,n):
#     dic [nums[i]] =0
# j=0
# for key in dic:
#     nums[j]=key
#     j+=1
# print(j)
# print(nums)