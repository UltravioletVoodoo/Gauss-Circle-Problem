import time

def start():
	n = raw_input("how many entries do you want?")
	n = int(n)
	startTime = time.time()
	for x in range(2,(n+2)):
		print triangular(x)
	endTime = time.time()
	TotalTime = endTime - startTime
	print "Completion time: %f"%TotalTime
	endingString = raw_input("Press Enter to Exit")
	
	
def triangular (n):
	return (n)*(n+1)/2


start()