li=[4,5,8,1,9,19,12,8,1,2]
length=len(li)
count=1
comp=0
while(count<length):
    for i in range(length-count):
        comp+=1
        if(li[i]>li[i+1]):
            temp=li[i]
            li[i]=li[i+1]
            li[i+1]=temp
    count+=1
print(comp)
print(li)