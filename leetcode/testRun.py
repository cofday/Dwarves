#__author__ = 'linweizhong'
from node import  *
from LRUCache import  *

s = LRUCache(2)
s.set(2,1)
s.set(2,2)
s.head.printLink()

s.get(2)
s.set(1,1)
s.head.printLink()
s.set(4,1)
s.head.printLink()
s.get(2)
s.head.printLink()







