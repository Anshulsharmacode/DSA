nums = [-2 , 1 , -3 , 4 , -1 , 2 ,1 , -5 ,4]



# kadne algo 
total = 0
maxi = float('-inf')
for i in range(0 , len(nums)):
    total = total +nums[i]
    maxi = max(maxi , total)
    if total <0:
        total=0

print(maxi)



# total = 0 
# maxi = float('-inf')
# for i in range(0 , len(nums)):
#     total= 0
#     for j in range(i , len(nums)):
#         total = total + nums[j]
#         maxi = max(maxi , total)

# print(maxi)
    
