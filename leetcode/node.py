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


class TreeNode :
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

    def printTree(self):
        print self.val
        if self.left != None :
            self.left.printTree()
        if self.right != None :
            self.right.printTree()

class Point :
    def __init__(self,a=0,b=0):
        self.x = a
        self.y = b
class RandomListNode:
    def __init__(self,x):
        self.label = x
        self.next  = None
        self.random = None




