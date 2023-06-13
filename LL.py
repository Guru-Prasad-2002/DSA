class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next 

class Linked_list:
    def __init__(self):
        self.head=None 
    def get_len(self):
        count=0 
        itr=self.head 
        while(itr!=None):
            count=count+1 
            itr=itr.next 
        return count
    def display(self):
        itr=self.head
        ans=""
        while(itr!=None):
            ans=ans+itr.data+"-->" 
            itr=itr.next 
        print(ans[0:len(ans)-3])
    def insert_beginning(self,value):
        newNode=Node(value,self.head)
        self.head=newNode
    def delete_beginning(self):
        if(self.head==None):
            print("EMPTY LL!Cannot Delete")
            return 
        else:
            self.head=self.head.next 
            return
    def insert_at_index(self,value,index):
        if(index<0 or index>self.get_len()+1):
            print("Invalid Index")
            return 
        itr=self.head
        newNode=Node(value,None)
        count=1
        while(count<index-1):
            itr=itr.next 
            count=count+1
        newNode.next=itr.next
        itr.next=newNode
        return 
    def delete_at_index(self,index):
        if(index<0 or index>self.get_len()+1):
            print("Invalid Index")
            return 
        return 
        if(index==1):
            self.delete_beginning()
            return
        itr=self.head
        count=1
        while(count<index-1):
            itr=itr.next 
            count=count+1
        itr.next=itr.next.next
        return 

ll=Linked_list()
ll.insert_beginning("3")
ll.insert_beginning("2")
ll.insert_beginning("1")
ll.display()
ll.delete_beginning()
ll.display()
ll.delete_beginning()
ll.display()
ll.insert_beginning("2")
ll.display()
ll.delete_at_index(1)
ll.delete_at_index(2)
ll.display()

