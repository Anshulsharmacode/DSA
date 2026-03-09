# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

input = [2,7,11,15,1,7]
target = 9
n= len(input)
i=0
j=1

for i in range(0,n-1):
    for j in range(i+1,n):
        if input[i]+input[j]== target:
            print(i,j)
        else:
            i+=1
            j+=1
        








# def two_sum(number , output):
#     num_dict ={}
#     for i in range(len(number)):
#         num_dict[i]= num_dict.get(i , 0)+1

#     for i in range(len(number)):
#         complement = target - number[i]
#         if complement in num_dict:
#             return (i, num_dict[complement])
#     return None

# print(two_sum(input, target))