# Iterative Python program to search an element 
# in linked list 
  
# Node class 
class Node: 
      
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 
  
# Linked List class 
class LinkedList: 
    def __init__(self): 
        self.head = None # Initialize head as None 
  
    # This function insert a new node at the 
    # beginning of the linked list 
    def push(self, new_data): 
      
        # Create a new Node 
        new_node = Node(new_data) 
  
        # 3. Make next of new Node as head 
        new_node.next = self.head 
  
        # 4. Move the head to point to new Node 
        self.head = new_node 
  
    # This Function checks whether the value 
    # x present in the linked list  
    def search(self, x): 
  
        # Initialize current to head 
        current = self.head 
  
        # loop till current not equal to None 
        while current != None: 
            if current.data == x: 
                return True # data found 
              
            current = current.next
          
        return False # Data Not found 
  
  
# Code execution starts here 
if __name__ == '__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    ''' Use push() to construct below list 
        14->21->11->30->10 '''
    llist.push(10); 
    llist.push(30); 
    llist.push(11); 
    llist.push(21); 
    llist.push(14); 
  
    if llist.search(21): 
        print("Yes") 
    else: 
        print("No") 
        
        
        
        
        

















# Recursive Python program to  
# search an element in linked list 
  
# Node class 
class Node: 
      
    # Function to initialise  
    # the node object 
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 
  
class LinkedList: 
      
    def __init__(self): 
        self.head = None # Initialize head as None 
  
    # This function insert a new node at  
    # the beginning of the linked list 
    def push(self, new_data): 
      
        # Create a new Node 
        new_node = Node(new_data) 
  
        # Make next of new Node as head 
        new_node.next = self.head 
  
        # Move the head to  
        # point to new Node 
        self.head = new_node 
      
      
    # Checks whether the value key  
    # is present in linked list  
    def search(self, li, key): 
          
        # Base case 
        if(not li): 
            return False
          
        # If key is present in  
        # current node, return true 
        if(li.data == key): 
            return True
          
        # Recur for remaining list 
        return self.search(li.next, key) 
      
# Driver Code             
if __name__=='__main__': 
  
    li = LinkedList() 
      
    li.push(1) 
    li.push(2) 
    li.push(3) 
    li.push(4) 
      
    key = 4
      
    if li.search(li.head,key): 
        print("Yes") 
    else: 
        print("No") 
