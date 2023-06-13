import bisect 
# Bisect Left ... Return the leftmost occurrence of an element if it is present .... else it returns the leftmost place in which element can be inserted in the array to maintain the sorted property of the array
arr=[1,2,2,2,4,5,6,7,9,9]
a=bisect.bisect_left(arr, -1)
b=bisect.bisect_left(arr,3)
print(a)
print(b)
if(arr[b]!=100):
    print("Not Found")
# Bisect Right ... Only returns the Rightmost place in which element can be inserted in the array to maintain the sorted property of the array
arr=[1,2,2,2,4,5,6,7,9,9]
a=bisect.bisect_right(arr, 2)
b=bisect.bisect_right(arr,3)
print(a)
print(b)
if(arr[b]!=100):
    print("Not Found")