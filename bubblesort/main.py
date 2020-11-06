import bubblesort,time
arr = bubblesort.arrMaker(1,25000,100)
print("before sort(start and end 5 numbers):",arr[0:5],"...",arr[-5:])
print("------bubbleSorting------")
start=time.time()
arr = bubblesort.bubbleSort(arr)
print("-----completed  sort-----")
print("after sort(start and end 5 numbers):",arr[0:5],"...",arr[-5:])
print("time used to sort:",time.time()-start)
