import copy
arr1=[]
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
def selection_sort(arr):
    arr1=copy.copy(arr)
    for i in range(len(arr)-1):
        min=arr[i]
        for j in range(i,len(arr)):
            if(arr1[j]<min):
                min=arr1[j]
                min_id=j
        var=arr1[min_id]
        arr1[min_id]=arr1[i]
        arr1[i]=var
    return arr1
print(selection_sort(arr1))