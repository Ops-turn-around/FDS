	
row1=int(input("Enter the number of rows in matrix : "))
non1=int(input("Enter the number of non zero enteries in sparse matrix : "))
sparse1=[[row1,3,non1]]
for i in range(non1):
    x=int(input("Enter row number : "))
    y=int(input("Enter column number : "))
    z=int(input("Enter value : "))
    sparse1.append([x,y,z])
row2=int(input("Enter the number of rows in matrix : "))
non2=int(input("Enter the number of non zero enteries in sparse matrix : "))
sparse2=[[row2,3,non2]]
for i in range(non2):
    x=int(input("Enter row number : "))
    y=int(input("Enter column number : "))
    z=int(input("Enter value : "))
    sparse2.append([x,y,z])
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
def simple_transpose(sp1):
    ret=[[sp1[0][1],sp1[0][0],sp1[0][2]]]
    for i in range(sp1[0][1]):
        for j in range(len(sp1)):
            if(sp1[j][1]==i):
                ret.append([sp1[j][1],sp1[j][0],sp1[j][2]])
    return ret
# def fast_transpose(sp1):
#     ret=[[0 for x in range(3)] for y in range(sp1[0][2]+1)]
#     ret[0][0]=sp1[0][1]
#     ret[0][1]=sp1[0][0] 
#     ret[0][2]=sp1[0][2]
#     cols=[0]
#     for i in range(sp1[0][1]):
#         sum=0
#         for j in range(1,sp1[0][2]+1):
#             if(sp1[j][1]==i):
#                 sum+=1
#         cols.append(sum)
#     pos=[0]
#     for i in range(1,len(cols)):
#         pos.append(cols[i]+pos[i-1])
#     for i in range(1,sp1[0][2]+1):
#         ret[pos[sp1[i][1]]]=sp1[i][0]
#         ret[pos[sp1[i][0]]]=sp1[i][1]
#         ret[pos[sp1[i][2]]]=sp1[i][2]
#         pos[sp1[i][1]]+=1
#     return ret

    # for i in range(sp1[0][2]):
        
            
# m1=[[3,3,6],[0,0,1],[0,2,3],[1,0,1],[1,2,4],[2,0,2],[2,1,1]]
# print(fast_transpose(m1))
print("Sum of sparse matrices : ",add(sparse1,sparse2))
print("Transpose of first sparse matrix is : ",simple_transpose(sparse1))