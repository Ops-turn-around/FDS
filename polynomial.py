degree1=int(input("Enter the highest degree of the polynomial 1: "))
terms1=int(input("Enter the number of terms in the polynomial 1: "))
poly1=[0 for x in range(degree1+1)]
for i in range(terms1):
    x=int(input("enter the degree : "))
    y=int(input("Enter the cofficient : "))
    poly1[x]=y
degree2=int(input("Enter the highest degree of the polynomial 2: "))
terms2=int(input("Enter the number of terms in the polynomial 2: "))
poly2=[0 for x in range(degree2+1)]
for i in range(terms2):
    x=int(input("enter the degree : "))
    y=int(input("Enter the cofficient : "))
    poly2[x]=y
print("Polynomial 1 is : ",poly1)
print("Polynomial 2 is : ",poly2)
def sum(poly1,size1,poly2,size2):
    if(size1>size2):
        poly3=[0 for x in range(size1)]
        poly3=poly1[:]
        for i in range(size2):
            poly3[i]+=poly2[i]
        return poly3[::-1]
    else:
        poly3=[0 for x in range(size2)]
        poly3=poly2[:]
        for i in range(size1):
            poly3[i]+=poly1[i]
        return poly3[::-1]
print("Sum of polynomial 1 & polynomial 2 is : ",sum(poly1,degree1+1,poly2,degree2+1))
x=int(input("Enter the value of X for which you want to evaluate polynomial 1 :"))
def value(poly,val):
    ret=0
    for i in range(len(poly)):
        ret+=((poly[i])*(val**i))
    return ret
print("The value of polynomial 1 at X=%d is %d"%(x,value(poly1,x)))
def multiply(poly1,poly2):
    poly3=[0 for x in range(len(poly1)+len(poly2)-1)]
    for j in range(len(poly1)):
        for k in range(len(poly2)):
            poly3[j+k]+=poly1[j]*poly2[k]
    return poly3[::-1]  
print(multiply(poly1,poly2))