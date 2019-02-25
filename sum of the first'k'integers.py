def k Largest(arr,k):
    arr.sort(reverse= True)
    for i in range(k):
        print (arr[i],end=" ")
arr=[1,28,82,90,30,42,5]
k=3
kLargest(arr,k)
