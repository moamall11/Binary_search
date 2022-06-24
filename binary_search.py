import random
import time

def naive_search(l,target):
	"""check every element of the list to get the target"""
	for i,element in enumerate(l):
		if element == target:
			return i


def binary_search(l,target,low=None,high=None):
	"""divide the list into two after every itiration"""
	#in the begining.
	if low is None:
		low=0
	if high is None:
		high=len(l)-1

	if high < low:
		return -1
	#find the middle point.
	midpoint=(low+high) // 2
	#if it's the target then return it.
	if target==l[midpoint]:
		return midpoint
	#if the target is bigger than the middle point 
	#then take the right half of the list and do the same with it.
	elif target > l[midpoint]:
		return binary_search(l,target,midpoint + 1,high)
	#if it's less do the same with the left half.
	else:
		#target < l[midpoint]
		return binary_search(l,target,low,midpoint - 1)

if __name__=='__main__':
	# l=[i for i in range(1,100,2)]
	# target=99
	# print(naive_search(l,target))numbers
	# print(binary_search(l,target))
	numbers=[]
	length=10000

	while len(numbers) < length:
		numbers.append(random.randint(-3*length,3*length))
	numbers=sorted(numbers)

	start=time.time()
	for target in numbers:
		naive_search(numbers,target)
	end=time.time()
	print("naive search time",(end-start),'seconds')

	start=time.time()
	for target in numbers:
		binary_search(numbers,target)
	end=time.time()
	print("binary search time",(end-start),'seconds')


