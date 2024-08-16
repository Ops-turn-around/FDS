r1=int(input("Enter the number of rows of matrix 1 :"))
c1=int(input("Enter the number of columns of matrix 1 :"))
r2=int(input("Enter the number of rows of matrix 2:"))
c2=int(input("Enter the number of columns of matrix 2 :"))
list1=[]
list2=[]
mat1=[]
mat2=[]
for i in range(r1):
    for j in range(c1):
        x=int(input("Enter the (%d,%d) element of matrix 1 : "%(i+1,j+1)))
        list1.append(x)
    mat1.append(list1)
    list1=[]
for i in range(r2):
    for j in range(c2):
        x=int(input("Enter the (%d,%d) element of matrix 2 : "%(i+1,j+1)))
        list2.append(x)
    mat2.append(list2)
    list2=[]
def triangular(mat1):
    if(len(mat1)!=len(mat1[0])):
        print("Not a square matrix")
    else:
        count=0
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                if(i>j and mat1[i][j]!=0):
                    count+=1
    if(count==0):
        print("Upper triangular matrix")
    elif(count>0):
        print("Not upper triangular")


def sum(mat1,mat2):
    if(len(mat1)!=len(mat2) or len(mat1[0])!=len(mat2[0])):
        return "Orders are diiferent so sum is not possible."
    else:
        mat3=mat1.copy()
        for i in range(len(mat2)):
            for j in range(len(mat2[0])):
                mat3[i][j]+=mat2[i][j]
        return mat3
trsp = [[0 for x in range(len(mat1[0]))] for y in range(len(mat1))] 
def transpose(mat1):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            trsp[i][j]=mat1[j][i]
    return trsp
def trace(mat1):
    sum=0
    if(len(mat1)!=len(mat1[0])):
        return "Not a sqaure matrix so no trace."
    else:
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                if(i==j):
                    sum+=mat1[i][j]
        return sum
def multiply(mat1,mat2):
    mult=[[0 for x in range(len(mat1[0]))] for y in range(len(mat2))]
    if(len(mat1[0])!=len(mat2)):
        return "Matrix multiplication not possible."
    else:
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    mult[i][j]+=mat1[i][k]*mat2[k][j]
        return mult
def saddle_point(mat1,n):
    if(len(mat1[0])!=len(mat1)):
        print("Not a square matrix so no saddle point.")
        return
    for i in range(n):
        min=mat1[i][0]
        col=0
        for j in range(n):
            if(min>mat1[i][j]):
                min=mat1[i][j]
                col=j
        k=0
        for k in range(n):
            if(min<mat1[k][col]):
                break
            k+=1
    if(k==n):
        print("The value of saddle point is : ",min)
    else:
        print("There is no saddle point")
print("Transpose of matrix 1 : ",transpose(mat1))
print("Trace of matrix 1 : ",trace(mat1))
print("Sum of two matrices : ",sum(mat1,mat2))
print("Product of two matrices : ",multiply(mat1,mat2))
triangular(mat1)
saddle_point(mat1,3)