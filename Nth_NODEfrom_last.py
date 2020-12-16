class Node: 
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # This function is in LinkedList class. It inserts 
    # a new node at the beginning of Linked List. 
  
    def push(self, new_data): 
  
        # 1 & 2: Allocate the Node & 
        #     Put in the data 
        new_node = Node(new_data) 
  
        # 3. Make next of new Node as head 
        new_node.next = self.head 
  
        # 4. Move the head to point to new Node 
        self.head = new_node 
  
    # Returns data at given index in linked list 
    def getNth(self, index): 
        current = self.head  # Initialise temp 
        count = 0  # Index of current node 
  
        # Loop while end of linked list is not reached 
        while (current): 
            if (count == index): 
                return current.data 
            count += 1
            current = current.next
  
        # if we get to this line, the caller was asking 
        # for a non-existent element so we assert fail 
        assert(false) 
        return 0
  
  
# Driver Code 
if __name__ == '__main__': 
  
    llist = LinkedList() 
  
    # Use push() to construct below list 
    # 1->12->1->4->1 
    llist.push(1) 
    llist.push(4) 
    llist.push(1) 
    llist.push(12) 
    llist.push(1) 
  
    n = 3
    print("Element at index 3 is :", llist.getNth(n)) 
    
    











# linked list using recursion 
  
  
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
  
class LinkedList: 
    def __init__(self): 
        self.head = None
  
    ''' Given a reference (pointer to pointer) to the 
        head of a list and an int, push a new node on 
        the front of the list. '''
  
    def push(self, new_data):  # make new node and add 
                              # into LinkedList 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    def getNth(self, llist, position): 
  
        # call recursive method 
        llist.getNthNode(self.head, position, llist) 
  
    # recursive method to find Nth Node 
    def getNthNode(self, head, position, llist): 
        count = 0  # initialize count 
        if(head): 
            if count == position:  # if count is equal to position, 
                                  # it means we have found the position 
                print(head.data) 
            else: 
                llist.getNthNode(head.next, position - 1, llist) 
        else:  # if head doesn't exist we have 
              # traversed the LinkedList 
            print('Index Doesn\'t exist') 
  
  
# Driver Code 
if __name__ == "__main__": 
    llist = LinkedList() 
    llist.push(1) 
    llist.push(4) 
    llist.push(1) 
    llist.push(12) 
    llist.push(1) 
    # llist.getNth(llist,int(input())) 
    # Enter the node position here 
    # first argument is instance of LinkedList 
  
    print("Element at Index 3 is", end=" ") 
    llist.getNth(llist, 3) 
