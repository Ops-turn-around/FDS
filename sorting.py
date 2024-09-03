import copy
arr1=[]
def swap(a,b):
    temp=a
    a=b
    b=temp
s1=int(int(input("Enter the number of elements in the array : ")))
for i in range(s1):
    x=int(input())
    arr1.append(x)
def bubble_sort(arr):
    comp1=0
    swps=0
    arr1=copy.copy(arr)
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            comp1+=1
            if(arr1[j]>arr1[j+1]):
                temp=arr1[j]
                arr1[j]=arr1[j+1]
                arr1[j+1]=temp
                swps+=1
        if(swps==0):
            break
    return arr1
def selection(arr):
    comp2=0
    for i in range(len(arr)-1):
        min=arr[i]
        min_id=-1
        for j in range(i+1,len(arr)):
            comp2+=1
            if(arr[j]<min):
                min=arr[j]
                min_id=j
        (arr[min_id],arr[i])=(arr[i],arr[min_id])
    return arr
def insertion(arr):
    comp3=0
    for i in range(1,len(arr)):
        j=i-1
        val=arr[i]
        comp3+=1
        while(j>=0 and arr[j]>val):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=val
    print("Insertion : ", comp3)
    return arr
def shellSort(arr):
    n = len(arr)
    gap = n/2
    comp=0
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            comp+=1
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap /= 2
    print(comp)
shellSort(arr1)
def digit_count(n):
    digits=0
    while(n>0):
        digits+=1
        n/=10
    return digits
def give_digit(n,x):
    for i in range(x):
        digit=n%10
        n/=10
    return digit
def bucket(arr):
    max=arr[0]
    for i in range(len(arr)):
        if(arr[i]>max):
            max=arr[i]
    total=digit_count(max)
    for k in range(total):
        buckets=[[] for x in range(10)]
        for i in range(len(arr)):
            digit=give_digit(arr[i],k+1)
            buckets[digit].append(arr[i])
        arr=[]
        for t in range(10):
            for j in range(len(buckets[t])):
                arr.append(buckets[t][j])
    return arr
 
