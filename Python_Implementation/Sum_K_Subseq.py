# Print subsequence of sum k
# def subseqsum(curr_sum,ind,target,ans,ds):
#     if(ind>len(ds)-1):
#         if(curr_sum==target):
#             print(ans)
#             return
#         else:
#             return
#     curr_sum+=ds[ind]
#     ans.append(ds[ind])
#     subseqsum(curr_sum,ind+1,target,ans,ds)
#     curr_sum-=ds[ind]
#     ans.pop()
#     subseqsum(curr_sum,ind+1,target,ans,ds)

# subseqsum(0,0,3,[],[3,1,2])

# Print only 1 subsequence of Sum K

# def subseqsum(curr_sum,ind,target,ans,ds):
#     if(ind>len(ds)-1):
#         if(curr_sum==target):
#             print(ans)
#             return True
#         else:
#             return False
#     curr_sum+=ds[ind]
#     ans.append(ds[ind])
#     if(subseqsum(curr_sum,ind+1,target,ans,ds)==True):
#         return True
#     curr_sum-=ds[ind]
#     ans.pop()
#     if(subseqsum(curr_sum,ind+1,target,ans,ds)==True):
#         return True
#     return False

# subseqsum(0,0,30,[],[3,1,2])

# Print the total number of Subsequence

def subseqsum(curr_sum,ind,target,ans,ds):
    if(ind>len(ds)-1):
        if(curr_sum==target):
            # print(ans)
            return 1
        else:
            return 0
    curr_sum+=ds[ind]
    ans.append(ds[ind])
    l=subseqsum(curr_sum,ind+1,target,ans,ds)
    curr_sum-=ds[ind]
    ans.pop()
    r=subseqsum(curr_sum,ind+1,target,ans,ds)==True
    return l+r

print(subseqsum(0,0,3,[],[3,1,2]))