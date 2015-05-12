import dis
import sys

def addStr1(s):
	return ">" + s + "<"

def addStr2(s):
	return ">%s<" % s

def addStr3(s,s2):
	return ">" + s + ":" + s2 + "<"

def addStr4(s,s2):
	return ">%s:%s<" % (s,s2)

def addStr5(s,s2,s3):
	return ">"+s+":"+s2+":"+s3+"<"

def addStr6(s,s2,s3):
	return ">%s:%s:%s<" % (s,s2,s3)

def addStr7(s,s2,s3,s4):
	return ">" + s + ":" + s2 + ":" + s3 + ":" + s4 + "<"

def addStr8(s,s2,s3,s4):
	return ">%s:%s:%s:%s<" % (s,s2,s3,s4)

def determineFunc(c):
	if c == 0:
		print("Please pass command line arguments equal to the number you'd like to run")
	elif c == 1:
		[addStr1(str(i)) for i in range(100000)]
	elif c == 2:
		[addStr2(str(i)) for i in range(100000)]
	elif c == 3:
		[addStr3(str(i),str(i)) for i in range(100000)]
	elif c == 4:
		[addStr4(str(i),str(i)) for i in range(100000)]
	elif c == 5:
		[addStr5(str(i),str(i),str(i)) for i in range(100000)]
	elif c == 6:
		[addStr6(str(i),str(i),str(i)) for i in range(100000)]
	elif c == 7:
		[addStr7(str(i),str(i),str(i),str(i)) for i in range(100000)]
	elif c == 8:
		[addStr8(str(i),str(i),str(i),str(i)) for i in range(100000)]
	else:
		print("Only 8 functions defined")

def main():
	determineFunc(len(sys.argv)-1)

if __name__ =='__main__':main()

