#!/bin/env python
import sys
iamlist=[]

for num in range(0,10):
	iamlist.append(num)
print iamlist

iamlist=[x*2 for x in range(0,10)]
print iamlist

iamdict={x:x*2 for x in range(0,10)}
print iamdict




