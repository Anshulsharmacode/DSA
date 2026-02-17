
def merge_sorted_lists(n, m):
    result = []
   
    i, j = 0, 0
    len_n = len(n)
    len_m = len(m)

    # Merge elements while both lists have remaining items
    while i < len_n and j < len_m:
        if n[i] <= m[j]:
            result.append(n[i])
            i += 1
        else:
            result.append(m[j])
            j += 1

    # Append remaining elements (if any)
    while i < len_n:
        result.append(n[i])
        i += 1

    while j < len_m:
        result.append(m[j])
        j += 1

    return result


def merge(arr):
    if len(arr)<= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr =arr [ : mid]
    right_arr= arr [mid : ]
    left = merge(left_arr)
    right = merge(right_arr)
    ans = merge_sorted_lists(left , right)
    return ans

arr = [ 2,3,5,6,3,2,5,7,1,5,4,7,8]
value = merge(arr)
print(value)
# print(result)