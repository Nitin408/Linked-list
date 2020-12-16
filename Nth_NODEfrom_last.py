# n'th node from end 
class Node: 
    def __init__(self, new_data): 
        self.data = new_data 
        self.next = None
      
class LinkedList: 
    def __init__(self): 
        self.head = None
  
    # createNode and and make linked list 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Function to get the nth node from  
    # the last of a linked list  
    def printNthFromLast(self, n): 
        temp = self.head # used temp variable 
          
        length = 0
        while temp is not None: 
            temp = temp.next
            length += 1
          
        # print count  
        if n > length: # if entered location is greater  
                       # than length of linked list 
            print('Location is greater than the' +
                         ' length of LinkedList') 
            return
        temp = self.head 
        for i in range(0, length - n): 
            temp = temp.next
        print(temp.data) 
  
# Driver Code         
llist = LinkedList()  
llist.push(20)  
llist.push(4)  
llist.push(15)  
llist.push(35) 
llist.printNthFromLast(4) 












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
