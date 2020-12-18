# Python program to count the number of time a given 
# int occurs in a linked list 
  
# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Counts the no . of occurrences of a node 
    # (search_for) in a linked list (head) 
    def count(self, search_for): 
        current = self.head 
        count = 0
        while(current is not None): 
            if current.data == search_for: 
                count += 1
            current = current.next
        return count 
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print temp.data, 
            temp = temp.next
  
  
# Driver program 
llist = LinkedList() 
llist.push(1) 
llist.push(3) 
llist.push(1) 
llist.push(2) 
llist.push(1) 
  
# Check for the count function 
print "count of 1 is % d" %(llist.count(1)) 









####################################################################################################################################################################
# Python program to count the number of  
# time a given int occurs in a linked list 
# Node class 
class Node: 
      
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
      
    # Function to initialize head 
    def __init__(self): 
        self.head = None
        self.counter = 0
          
    # Counts the no . of occurances of a node 
    # (seach_for) in a linkded list (head) 
    def count(self, li, key):      
          
        # Base case  
        if(not li):  
            return self.counter 
          
        # If key is present in  
        # current node, return true  
        if(li.data == key):  
            self.counter = self.counter + 1
          
        # Recur for remaining list  
        return self.count(li.next, key)  
  
    # Function to insert a new node  
    # at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the  
    # linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data) 
            temp = temp.next
  
# Driver Code 
llist = LinkedList() 
llist.push(1) 
llist.push(3) 
llist.push(1) 
llist.push(2) 
llist.push(1) 
  
# Check for the count function 
print ("count of 1 is", llist.count(llist.head, 1)) 












#############################################################################################################################################################
def count(self, temp, key): 
      
    # during the initial call, temp 
    # has the value of head 
      
    # Base case 
    if temp is None: 
        return 0
          
    # if a match is found, we  
    # increment the counter 
    if temp.data == key: 
        return 1 + count(temp.next, key) 
    return count(temp.next, key) 
      
# to call count, use 
# linked_list_name.count(head, key) 
