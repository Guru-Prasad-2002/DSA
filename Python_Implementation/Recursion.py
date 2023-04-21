# Print name n times

def name_fun(i,n,name):
    if(i==n):
        return 
    print(name)
    i+=1
    name_fun(i,n,name)

name_fun(1,5,"Guru")