__author__ = 'linweizhong'
"""
LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.


"""
class DqNode :
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
    def printLink(self):
        p = self
        str = ""
        while p :
            str = "%s %d:%d"%(str,p.key,p.val)
            p = p.next
        print str




class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.curSize  =  1
        self.key2value = {}
        self.head = DqNode(-1,-1)
        self.tail = DqNode(-1,-1)
        self.head.next  = self.tail
        self.tail.pre = self.head

    def moveTofirst(self,node):
        nodePre = node.pre
        nodeNext = node.next
        nodePre.next = nodeNext
        nodeNext.pre = nodePre
        self.insert(node)

    # @return an integer
    def get(self, key):
        if self.key2value.has_key(key):
            n = self.key2value[key]
            value = n.val
            self.moveTofirst(n)
            return value
        else :
            return  -1

    def insert(self,node):
        next = self.head.next
        self.head.next = node
        node.pre = self.head
        if next :
            node.next = next
            next.pre  = node
        else :
            node.next = None


    def moveLRU(self):
        mnode = self.tail.pre
        prenode = mnode.pre
        prenode.next  = self.tail
        self.tail.pre = prenode
        del self.key2value[mnode.key]

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.get(key) == -1:
            newNode  = DqNode(key,value)
            self.insert(newNode)
            if self.curSize <= self.capacity :
                self.curSize = self.curSize + 1
            else :
                self.moveLRU()
            self.key2value[newNode.key] = newNode
        else:
            self.key2value[key].val = value

        #self.head.printLink()



