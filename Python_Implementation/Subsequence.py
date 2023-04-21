# # Subsequence 
def subseq(ind,l,arr):
    if(ind>len(arr)-1):
        print(l)
        return
    # print(ind)
    l.append(arr[ind])
    subseq(ind+1,l,arr)
    l.pop()
    subseq(ind+1,l,arr)

subseq(0,[],[3,1,2])

