n= 1634

nod= len(str(n))
print (nod)

num =n 
result = 0

while num >0:
    last = num %10
    result += last**nod
    num = num //10

if (n==result):
    print(f"yes in palidrome number {result}")
else:
    print("not palidrome number ")

print(result)



