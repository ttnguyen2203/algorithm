import numpy as np
import random



# insertion sort

def insertion_sort(ls):
	if not ls:
		return []
	if len(ls) == 0:
		return []

	for i in range(1, len(ls)):
		val = ls[i]
		j = i - 1
		while j >= 0 and val < ls[j]:
			j -= 1
		ls.insert(j+1, val)
		ls.pop(i+1)
		print(ls)

	return ls

def merge_sort(ls):
	return None

def bubble_sort(ls):
	return None

def quick_sort(ls):
	#iterative
	def partition(ls):
		if len(ls) == 0  or len(ls) == 1:
			return ls
		pivot = random.choice(ls)
		less = []
		equal = []
		greater = []
		for n in ls:
			if n > pivot:
				greater.append(n)
			elif n < pivot:
				less.append(n)
			else:
				equal.append(n)
		final = []
		final.extend(partition(less))
		final.extend(equal)
		final.extend(partition(greater))
		return final

	return partition(ls)






##### test
ls = list(np.random.rand(10))
ls1 = [5, 3, 4, 2, 1,5, 3, 4, 2, 1]

alg = quick_sort(ls1)
truth = sorted(ls1)

print(alg == truth)
print(alg)
print(truth)


