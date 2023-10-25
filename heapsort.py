def deef(arr, n, i):
	largest = i 
	l = 2 * i + 1 
	r = 2 * i + 2 

	if l < n and arr[i] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i]) 


		deef(arr, n, largest)


def heapSort(arr):
	n = len(arr)

	for i in range(n // 2 - 1, -1, -1):
		deef(arr, n, i)



	for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i]) 
		deef(arr, i, 0)

arr = [134, 3, 23, 14, 78, 33, 233, 454, 9, 0]
heapSort(arr)
n = len(arr)
print('El arreglo acomodado es')
for i in range(n):
    print(arr[i])
