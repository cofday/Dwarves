#__author__ = 'linweizhong'
class ListNode :
    def __init__(self,x):
        self.val = x
        self.next = None

    def printList(self):
        istr  = "%d" % self.val
        p = self.next
        while p != None:
            istr = "%s %d" %(istr,p.val)
            p = p.next

        print(istr)
class Link :
    def __init__(self,list):
        if len(list) == 0 :
            self.head = None
        else :
            self.head  = ListNode(list[0])
            p = self.head
            for v in list[1:] :
                n = ListNode(v)
                p.next = n
                p = n
    def printLink(self):
        self.head.printList()



class TreeNode :
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def printTree(self):
        print self.val
        if self.left != None :
            self.left.printTree()
        #else:
        #    print "#"
        if self.right != None :
            self.right.printTree()
        #else:
        #   print("#")
"""
class binaryTree :
    def __init__(self):
        self.root = None

    def build(self,data):

        for item in data :
"""

class Point :
    def __init__(self,a=0,b=0):
        self.x = a
        self.y = b
class RandomListNode:
    def __init__(self,x):
        self.label = x
        self.next  = None
        self.random = None




