# recursion in python 987


count =0 



# -----------------head recursion --------------
# def fun():
#     global count
    
#     if (count == 4):
#         return
#     print("anshul")
#     count+=1
#     fun()

# fun()

# ------------------------ tail recursion --------------
# def fun():
#     global count
    
#     if (count == 4):
#         return
#     count+=1
#     fun()
#     print("anshul")
    

# fun()


def fun(x,n):
    if n==0:
        return
    print(x)
    fun(x,n-1)

fun(5,6)