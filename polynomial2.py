t1=int(input("Enter the number of terms in polynomial 1 : "))
li1=[]
for i in range(t1):
    sublist1=[]
    power=int(input("Enter the power of variable : "))
    cofficient=int(input("Enter the cofficient : "))
    sublist1.append(power)
    sublist1.append(cofficient)
    li1.append(sublist1)
t2=int(input("Enter the number of terms in polynomial 2 : "))
li2=[]
for i in range(t2):
    sublist2=[]
    power=int(input("Enter the power of variable : "))
    cofficient=int(input("Enter the cofficient : "))
    sublist2.append(power)
    sublist2.append(cofficient)
    li2.append(sublist2)
print(li1)
print(li2)
def add(li1,li2,t1,t2):
    c1=0
    c2=0
    ret=[]
    while(c1<t1 and c2<t2):
        if(li1[c1][0]==li2[c2][0]):
            ret.append([li1[c1][0],li1[c1][1]+li2[c1][1]])
            c1+=1
            c2+=1
        elif(li1[c1][0]>li2[c2][0]):
            ret.append([li1[c1][0],li1[c1][0]])
            c1+=1
        else:
            ret.append([li2[c2][0],li2[c2][1]])
            c2+=1
    while(c1<t1):
        ret.append([li1[c1][0],li1[c1][1]])
        c1+=1 
    while(c2<t2):
        ret.append([li2[c2][0],li2[c2][1]])
        c2+=1
    return ret
print("The sum of polynomial 1 & polynomial 2 is : ",add(li1,li2,t1,t2))
def produx(li1,li2,t1,t2):
    ret=[]
    for i in range(t1):
        for j in range(t2):
            t=1
            for k in range(len(ret)):
                if(li1[i][0]+li2[j][0]==ret[k][0]):
                    ret[k][1]+=li1[i][1]*li2[j][1]
                    t=0
            if(t==1):
                ret.append([li1[i][0]+li2[j][0],li1[i][1]*li2[j][1]])
    return ret
print(produx(li1,li2,t1,t2))


