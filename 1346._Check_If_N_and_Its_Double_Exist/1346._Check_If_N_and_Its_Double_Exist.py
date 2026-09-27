arr = [10,2,5,3]


i=0
while i < len(arr):
    j = 0

    while j < len(arr):
            if i != j and arr[i] == 2 * arr[j]:
                print(True)
            j += 1
    i+=1
    print(False)  