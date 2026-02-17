q= "qewjasdbfgsdg"
s = ['s', 'a', 'g', 's', 'w']   

result =dict()
for i in q:
    result[i]= result.get(i,0)+1


for j in s:
    print(j , result.get(j,0))


# print(result)