class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self,head):
        self.head=head
    def insertbegin(self,node):
        node.next=self.head
        self.head=node
        print(node.data,'is inserted successfully in beginning')
    def insertpos(self,node,pos):
        if pos==1:
            node.next=self.head.next
            self.head=node
        else:
            prev=self.head
            for i in range(1,pos-1):
                prev=prev.next
            node.next=prev.next
            prev.next=node
            print(node.data,'is inserted successfully at %d position'%pos)
    def insertend(self,node):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=node
        print(node.data,'is inserted successfully at end')
    def display(self):
        temp=self.head
        if temp.data is None:
            print('List is empty')
        else:
            while temp.next is not None:
                print(temp.data,'-->',end=' ')
                temp=temp.next
            print(temp.data)
            
n1=Node(20)
l1=LinkedList(n1)
l1.insertbegin(Node(10))
l1.insertend(Node(30))
l1.insertend(Node(40))
l1.insertend(Node(50))
l1.insertpos(Node(22),1)
l1.insertpos(Node(55),5)
l1.display()
