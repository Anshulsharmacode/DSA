##worst solution

# num =20  
# result =[]

# for i in range(1, num+1):
#   if num % i ==0:
#     result.append(i)

# print(result)

# ##tc -o(n)
# ##sc- o(n)

# avg case

# num = 20

# result = []

# for i in range(1, num //2):
#     if num % i ==0:
#         result.append(i)
    
# result.append(num)
# print(result)

##optimal case

from math import sqrt

num =36

result = []

for i in range (1 , int(sqrt(num))+1):
    if num %i ==0:
        result.append(i)
        if num //i != i:
            result.append(num //i)
result.sort()  ##tc- o(nlogn )
print(result)

# tc- o(sqr(n))+ O(nlog)
# sc- O(k)