
'''HeapSort'''
import random
import time
import array 
import sys
sys.setrecursionlimit(50000)
generatedArraySize = 20000

def generateRandomArray():
    array = []
    for x in range(generatedArraySize):
       array.append(random.randint(1, 100))
    return array;

def generateSortAscendingArray():
    array = []
    for x in range(generatedArraySize):
       array.append(x)
    return array;
    
def generateSortDescendingArray():
    array = []
    for x in range(generatedArraySize):
       array.append(generatedArraySize - x)
    return array;
    
def max_heapify(a: array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and a[left] > a[i]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right
    if i != largest:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, n, largest)
def build_max_heap(a: array):
    n = len(a) - 1
    for i in range((n // 2), -1, -1):
        max_heapify(a, n, i)
def heap_sort(a: array):
    build_max_heap(a)
    n = len(a) - 1
    for i in range(n, 0, -1):
        a[i], a[0] = a[0], a[i]
        max_heapify(a, i, 0)
A = generateSortAscendingArray()
A2 = generateSortDescendingArray()
A3 = generateRandomArray()

print("Heap Sort")
start_time = time.time()
heap_sort(A)
print("--- %s seconds --- (tablica A - posortowana)" % (time.time() - start_time)) 

start_time = time.time()
heap_sort(A2)
print("--- %s seconds --- (tablica A2  - odwrotnie posortowana)" % (time.time() - start_time))

start_time = time.time()
heap_sort(A3)

print("--- %s seconds --- (tablica A3 losowe wartości)" % (time.time() - start_time))
print (end=" ")


'''Quick Sort'''
def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)
def partition(A, p, r):
    pivot = A[r]
    smaller = p
    for i in range(p, r):
        if A[i] <= pivot:
            A[smaller], A[i] = A[i], A[smaller]
            smaller = smaller + 1
    A[smaller], A[r] = A[r], A[smaller]
    return smaller

print ("Quick Sort")
start_time = time.time()
quick_sort(A, 0, len(A) - 1)
print("--- %s seconds ---(tablica A - losowe wartosci)" % (time.time() - start_time))

start_time = time.time()
quick_sort(A2, 0, len(A2) - 1)
print("--- %s seconds ---(tablica A2 - posortowana)" % (time.time() - start_time))

start_time = time.time()
quick_sort(A3, 0, len(A3) - 1)
print("--- %s seconds ---(tablica A3 - odwrotnie posortowana)" % (time.time() - start_time))
print (end=" ")

'''Buuble Sort'''
def bubbleSort(array):
	n = len(array)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if array[j] > array[j+1] :
				array[j], array[j+1] = array[j+1], array[j]

print ("Bubble Sort")
start_time = time.time()
bubbleSort(A)
print("--- %s seconds --- (tablica A - losowe wartosci)" % (time.time() - start_time))

start_time = time.time()
bubbleSort(A2)
print("--- %s seconds --- (tablica A2 - posortowana)" % (time.time() - start_time))

start_time = time.time()
bubbleSort(A3)
print("--- %s seconds --- (tablica A3 - odwrotnie posortowana)" % (time.time() - start_time))

