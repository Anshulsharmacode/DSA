arr = [10,2,5,3]


i=0 
j=1


while j< len(arr)-1:
    if arr[i]==arr[j]*arr[j+1]:
        print(True)
    j+=1