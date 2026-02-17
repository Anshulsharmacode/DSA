n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 11, 1, 9, 5, 67, 2]

# ----------------using dict ------------

result = dict()

for i in n:
    result[i]= result.get(i , 0)+1

print(result)

for j in m :
    print(result.get(j,0))





# ---------------------------avg case-------------------

# has = [0]*11
# # print(has)

# for num in n:
#     has[num]+=1

# for nums in m:
#     if 1 <= nums <= 10:   
#         print(has[nums])
#     else:
#         print("0")





# ----------------------------------brute------------------------------------------------------

# for i in m :
#     print("i",i)
#     count = 0 
#     for x in n:
#         if x==i:
#             count +=1

#     print(count)



# --------------------------------------------------------------------------------------------------------------------
# result = {}

# for value in m:
    
#     count = n.count(value)
#     if count > 0:
#         result[value] = count

# print(result)