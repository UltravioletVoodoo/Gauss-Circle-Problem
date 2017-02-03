#############################################
#NAME: BEZEAUGENERATOR.PY
#AUTHOR: JONATHAN BEZEAU
#PURPOSE: TO GENERATE A BEZEAU NUMBER AND ITS CORRESPONDING APPROXIMATION FOR PI
#############################################



import sys
import math
import time

	
def Start():
	n = raw_input("How many approximation do you want?")
	n = int(n)
	startTime = time.time()
	for x in range (2,n+2):
		Generate(x)
	endTime = time.time()
	TotalTime = endTime - startTime
	print "Completion time: %f"%TotalTime
	endingString = raw_input("Press Any Key To Exit")
	
	
def Generate(n):
	T = float(n*(n+1)/2)
	List = Create_Dots(n)
	Sliver_Dots = float(Count_Dots(List,(n-1)))
	B_Nums = 2*(Sliver_Dots + T)
	print B_Nums/T
	


def Create_Dots(n):
	lines = int(math.ceil(math.sqrt(2)*n - n))
	List = []
	for x in range(lines):
		y = n - 1
		while(x < n):
			List = List + [[x,y]]
			x = x + 1
			y = y - 1
	return List
	
def Count_Dots(List, n):
	counter = 0
	for x in List:
		if (math.sqrt(x[0]**2 + x[1]**2) <= n):
			counter = counter + 1
	return counter - (n + 1)

	
	
	
	
	
Start()