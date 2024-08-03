class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
    
    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while temp.next is not None:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value
    
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp.value
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp

    def set(self,index,value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert (self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            self.prepend(value)
        if index==self.length:
            self.append(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True

    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        temp=self.get(index-1)
        node_to_remove=temp.next
        temp.next=node_to_remove.next
        node_to_remove.next=None
        self.length-=1
        return node_to_remove
    
    def reverse(self):
        current=self.head
        self.head=self.tail
        self.tail=current
        before=None
        after=current.next
        for _ in range(self.length):
            after=current.next
            current.next=before
            before=current
            current=after
    


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.prepend(0)
my_linked_list.print_list()
print()
print("Popped Item: ",my_linked_list.pop())
my_linked_list.print_list()
print()
print("Popped Item: ",my_linked_list.pop_first())
print()
my_linked_list.print_list()
print("Item at index 1: ",my_linked_list.get(1).value)
print()
my_linked_list.set(1,4)
my_linked_list.print_list()
print()
my_linked_list.insert(1,5)
my_linked_list.print_list()
print()
my_linked_list.remove(1)
my_linked_list.print_list()
print()
my_linked_list.reverse()
my_linked_list.print_list()