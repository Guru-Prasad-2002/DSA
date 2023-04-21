import numpy as np
# create a random arra with 15 elements
arr = np.random.randint(0, 100, 15)
print(arr)

def merge_sort(arr,low,high):
    if(low==high):
        return 
    mid=(low+high)//2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    temp=[]
    ptr1=low
    ptr2=mid 
    while(ptr1<low and ptr2<high):
        if(arr[ptr1]<=arr[ptr2]):
            temp.append(arr[ptr1])
            ptr1+=1
        if(arr[ptr2]<arr[ptr1]):
            temp.append(arr[ptr2])
            ptr2+=1
        if(ptr1==mid):
            while(ptr2!=high):
                temp.append(arr[ptr2])
        if(ptr2==high):
            while(ptr2!=high):
                temp.append(arr[ptr2])

merge_sort(arr, 0, 14)
print(arr) 


