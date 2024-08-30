import copy
arr1=[]
def swap(a,b):
    temp=a
    a=b
    b=temp
s1=int(int(input("Enter the number of elements in the array : ")))
for i in range(s1):
    x=int(input("Enter element %d : "%(i+1)))
    arr1.append(x)
def bubble_sort(arr):
    arr1=copy.copy(arr)
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            if(arr1[j]>arr1[j+1]):
                temp=arr1[j]
                arr1[j]=arr1[j+1]
                arr1[j+1]=temp
    return arr1
def selection(arr):
    for i in range(len(arr)-1):
        min=arr[i]
        min_id=-1
        for j in range(i+1,len(arr)):
            if(arr[j]<min):
                min=arr[j]
                min_id=j
        (arr[min_id],arr[i])=(arr[i],arr[min_id])
    return arr
def insertion(arr):
    for i in range(1,len(arr)):
        j=i-1
        val=arr[i]
        while(j>=0 and arr[j]>val):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=val
    return arr
print(insertion(arr1))
