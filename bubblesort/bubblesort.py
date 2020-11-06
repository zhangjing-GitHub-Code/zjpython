def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
	        if (arr[j] < arr[j + 1]):
		        arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def arrMaker(a,b,qty):
    import random
    arr=[]
    for i in range(qty):
	    arr.append(random.randint(a,b))
    return arr
