lmn=int(input())
a=0
for i in range(1,lmn):
    if(lmn%i==0):
        a+=1
    else:
        continue
if(a==1):
    print("yes")
else:
    print("no") 
