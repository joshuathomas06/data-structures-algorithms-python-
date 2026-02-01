class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
class Doubly_Linked_List:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    #print a DLL
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #appen to a DLL O(1)
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        temp = self.tail 
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.length = new_node
            self.tail = new_node
        else:
             new_node.next = self.head
             self.head.prev = new_node
             self.head = new_node
        self.length += 1
        return True
    
    
    
        



    
            

        


#TEST/IMPLEMENT
dll = Doubly_Linked_List(10)
dll.print() #need parantheses to call method