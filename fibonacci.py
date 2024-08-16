
# size=int(input("Enter the size of the array : "))
# li=[]
# for i in range(size):
#     x=int(input("Enter the element %d of the array : "%(i+1)))
#     li.append(x)
def fib(n):
    if(n==1):
        return 0
    elif(n==2 or n==3):
        return 1
    else:
        return fib(n-2)+fib(n-1)
def ret(n):
    num=0
    x=1
    while(num<n):
        num=fib(x)
        x+=1
    return num

