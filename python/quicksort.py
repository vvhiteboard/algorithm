

def parseInput(inputValue) :
	arr = inputValue.split(",")
	result = []

	for val in arr :
		result.append(int(val.strip()))

	return result


def partition(arr, pivotIndex) :
	if len(arr) <= 1:
		return ([], [], arr)

	pivot = arr[pivotIndex]

	less = []
	great = []
	equal = []

	for val in arr :
		if val < pivot :
			less.append(val)
		elif val > pivot:
			great.append(val)
		else :
			equal.append(val)

	return (less, great, equal)


def quickSort(arr) :
	if len(arr) <= 0:
		return arr
		
	(less, great, equal) = partition(arr, 0)

	less = quickSort(less)
	great = quickSort(great)

	result = []
	result.extend(less)
	result.extend(equal)
	result.extend(great)

	return result


if __name__ == "__main__" :
	inputValue = input()

	arr = parseInput(inputValue)

	print("before : ", arr)

	arr = quickSort(arr)

	print("after : ", arr)