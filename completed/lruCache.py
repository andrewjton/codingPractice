#https://leetcode.com/problems/lru-cache/description/

class LRUCache:
    #use a dictionary to store the Nodes you're using
    #use a linkedlist to order the Nodes from first accessed to last accessed.
    
    #get: check your cache dict for key
        #if it exists, remove & add it back to the LL. return the node's value
        #if it doesn't exist, return -1 
    #put: check your cache dict for key
        #if it exists remove & add it back to the LL. return the node's value
        #if not, remove the node after the head of the LL
        #in both cases, you have to check that the dict's len doesn't exceed capacity
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = dict()
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            n = self.cache[key]
            self.__removeFromLL(n)
            self.__addToLL(n)
            return n.value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            n = self.cache[key]
            self.__removeFromLL(n)
            newNode = Node(key, value)
            self.__addToLL(newNode)
            self.cache[key] = newNode
        else:
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.__addToLL(newNode)
            
        if (len(self.cache) > self.capacity):
            lRUNode = self.head.next
            del self.cache[lRUNode.key]
            self.head.next = lRUNode.next
            self.head.next.prev = self.head
            

    def __addToLL(self, node):
        #add to the tail of the LL
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node