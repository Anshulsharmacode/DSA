num =[1,2,3,4,5,6,7]
left= 0
right = 6

def rev(num, left, right):
    # lenth = num.len()

    if left>=right:
        return
    num[left],num[right]= num[right],num[left]

    rev(num, left+1, right-1)

rev(num,left, right)
print(num)