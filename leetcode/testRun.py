#__author__ = 'linweizhong'
from node import  *
#from  wordBreakII import  *
#from  SingleNumber import  *
from buildTreefromPreorderInorderTraversal import  *
s = Solution()
A = ["A","B","D","E","C","F"]
B = ["D","B","E","A","F","C"]
A = [1,2]
B = [2,1]
t= s.buildTree(A, B)
t.printTree()






