li=[]
leng=int(input("enter the number of elements in the list : "))
for  i in range(leng):
    x=int(input("Enter the element %d : "%(i+1)))
    li.append(x)
#LINEAR SEARCH
key=int(input("Enter the key you want to search : "))
count=1
comp1=0
for i in range(len(li)):
    comp1+=1
    if(key==li[i]):
        print("Key found using linear search at index %d "%i)
        count=0
        break
if(count==1):
    print("Key not found.")
#BINARY SEARCH
h=leng-1
l=0
comparison=0
while(h>=l):
    mid=int((h+l)/2)
    comparison+=1
    if(key==li[mid]):
        print("Key found using binary search at index %d "%mid)
        break
    elif(key>li[mid]):
        l=mid+1
    else:
        h=mid-1
if(l>h):
    print("Key not found.")
print(comparison,"binary\n")
print(comp1," linear ")
#sentinel search
li3=li.copy()
li3.append(key)
i=0
while(li3[i]!=key):
    i+=1
if(i<len(li3)-1):
    print("Key found at index %d."%i)
else:
    print("Key not found.")