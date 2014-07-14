#!/bin/env python


def basicWay(arry):
	values=0
	for item in arry :
		values = values + item
	return values

def rightWay(arry):
	return sum(arry)

def mulBasicWay(arry):
	values = 1 
	for item in arry:
		values *= item
	return values 

def mulRightWay(s):
	from operator import mul
	return reduce(mul,s)


s = [x  for x in range(1,10)  ]
print basicWay(s)
print rightWay(s)
print mulBasicWay(s)
print mulRightWay(s)


