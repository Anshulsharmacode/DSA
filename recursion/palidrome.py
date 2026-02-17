n = "nitin"
l= len(n)-1
# left= 0
# right=l-1

# while left<right:
#     if n[left]!=n[right]:
#         print('false')

#     left+=1
#     right-=1
#     print("true")   


def palidrome(n , left , right):
    if left >=right:
        return 'true'
    if n[left]!= n[right]:
        return 'false'
    
    return palidrome( n , left+1 , right-1)

    # return 'true'


print(palidrome(n , 0 , l ))

