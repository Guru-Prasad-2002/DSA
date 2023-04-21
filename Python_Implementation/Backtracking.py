# print 1 to N 

# def printing(i,N):
#     if(i==0):
#         return
#     printing(i-1,N)
#     print(i)

# printing(5,5)

# print N to 1 

# def printing(i,N):
#     if(i==N+1):
#         return
#     printing(i+1,N)
#     print(i)

# printing(0,5)

# Functional SUmmation of First N Numbers

def summation(N):
    if(N==1):
        return 1 
    return N+summation(N-1)

print(summation(5))

