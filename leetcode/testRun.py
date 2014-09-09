#__author__ = 'linweizhong'
from node import  *
#from  wordBreakII import  *
#from  SingleNumber import  *
from buildTreefromInorderPostorderTraversal import  *
s = Solution()
A = ["D","B","E","A","F","C"]
B = ["D","E","B","F","C","A"]
A = [2,1]
B = [2,1]
t= s.buildTree(A, B)
t.printTree()






