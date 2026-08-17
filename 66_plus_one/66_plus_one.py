digits = [1,2,3]

number= int("".join(map(str , digits)))
number+=1
final = list(map(int , str(number)))
# print("final", final)