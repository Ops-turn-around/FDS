from statistics import mode
a=int(input("Enter the  number of students : "))
sum=0
b=[]
for i in range (0,a):
    x=int(input("Enter the marks of student %d : " %(i+1)))
    b.append(x)
invalid=0
min=b[0]
max=b[0]
absent=0
fail=0
passed=0
for i in range(0,a):
    if(b[i]<101 and b[i]>=0 and b[i]!=0):
        sum+=b[i]
    if(b[i]>max):
        max=b[i]
    if(b[i]<min and b[i]!=-1):
        min=b[i]
    if(b[i]==-1):
        absent+=1
    if(b[i]<33):
        fail+=1
    if(b[i]>=33):
        passed+=1
    if(b[i]>100 or b[i]<0 and b[i]!=-1):
        invalid+=1
print("Minimum marks is : ",min)
print("Maximum marks is : ",max)
print("Average marks is : %f"%(sum/(a-absent)))
print("Number of absent students are : ",absent)
print("Percentage of sudents passed : %3f"%((passed*100)/a))
print("Percentage of sudents failed : %3f"%((fail*100)/a))
print("Number of invalid enteries : ",invalid)
print("Marks with highest frequency : ",mode(b))
