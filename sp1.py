def sparse():
    n = int(input("Enter th no of rows: "))
    m = int(input("Enter th no of cols: "))
    sparse = []
    count = 0
    for i in range(0,n):
        for j in range(0,m):
            a = int(input("Enter (%d,%d) element: "%(i,j)))
            if a!=0:
                sparse.append([i,j,a])
                count+=1
    sparse = [[n,m,count]] + sparse
    return sparse
sp1=sparse()
sp2=sparse()
def simple_transpose(sp1):
    ret=[[sp1[0][1],sp1[0][0],sp1[0][2]]]
    for i in range(sp1[0][1]):
        for j in range(len(sp1)):
            if(sp1[j][1]==i):
                ret.append([sp1[j][1],sp1[j][0],sp1[j][2]])
    return ret

def add(sp1,sp2):
    c1=c2=1
    ret=[]
    while(c1<len(sp1) and c2<len(sp2)):
        if(sp1[c1][0]==sp2[c2][0] and sp1[c1][1]==sp2[c2][1]):
            ret.append([sp1[c1][0],sp1[c1][1],sp1[c1][2]+sp2[c2][2]])
            c1+=1
            c2+=1
        elif(sp1[c1][0]==sp2[c2][0]):
            if(sp1[c1][1]>sp2[c2][1]):
                ret.append([sp2[c2][0],sp2[c2][1],sp2[c2][2]])
                c2+=1
            else:
                ret.append([sp1[c1][0],sp1[c1][1],sp1[c1][2]])
                c1+=1
        elif(sp1[c1][0]<sp2[c2][0]):
            ret.append([sp1[c1][0],sp1[c1][1],sp1[c1][2]])
            c1+=1
        elif(sp1[c1][0]>sp2[c2][0]):
            ret.append([sp2[c2][0],sp2[c2][1],sp2[c2][2]])
            c2+=1
    while(c1<len(sp1)):
        ret.append([sp1[c1][0],sp1[c1][1],sp1[c1][2]])
        c1+=1
    while(c2<len(sp2)):
        ret.append([sp2[c2][0],sp2[c2][1],sp2[c2][2]])
        c2+=1
    ret.insert(0,[sp1[0][0],sp1[0][1],len(ret)])
    return ret
def fast_transpose(sp1):
    sp2 = [[sp1[0][1],sp1[0][0],sp1[0][2]]] + [0]* sp1[0][2]
    freq = [0] * (sp1[0][1]+1)
    for i in sp1[1:]:
        freq[(i[1])+1] += 1
    freq[0]=1
    for i in range(1,len(freq)-1):
        freq[i] = freq[i-1]+freq[i]
    for i in sp1[1:]:
        sp2[freq[i[1]]] = [i[1],i[0],i[2]]
        freq[i[1]]+=1
    return sp2
print("Sum of sparse matrices is : ",add(sp1,sp2))
print("Simple transpose of matrix 1 : ",simple_transpose(sp1))
print("Simple transpose of matrix 2 : ",simple_transpose(sp2))
print("Fast transpose of matrix 1 : ",fast_transpose(sp1))
print("Fast transpose of matrix 2 : ",fast_transpose(sp2))
