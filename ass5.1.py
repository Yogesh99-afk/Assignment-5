list = [1,2,3,4,5,6,7,8,9,10]
a=[]
for i in list:
    if i <= 5:
        a.append(i)
        i+=1
    else:
        break
print(f"Extracted List :{a}")
a.reverse()
print(f"Reverse of Ex list : {a}")