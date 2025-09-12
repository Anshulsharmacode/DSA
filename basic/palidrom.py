n= 1234   
num = n 
rev= 0
while num >0:
    last = num %10
    rev =rev * 10 +last
    num = num //10
print(rev)
if (rev == n):
    print("true")
else:
    print("false")





# n= 121

# num =n 


# while num >0:
#     last = num %10
#     num =num// 10
#     if (last == n ):
#         print ("true")
#     else:{
#         print("False")
#     }

