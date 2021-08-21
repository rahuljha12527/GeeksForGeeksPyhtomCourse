


def merge(arr,low,mid,high):
    left=arr[low:mid+1]
    right=arr[mid+1:high+1]
    i=0
    j=0
    k=low

    while i<len(left) and j<len(right):

        if left[i]<right[j]:
            arr[k]=left[i]
            i=i+1
            k=k+1
        else:
            arr[k]=right[j]
            k=k+1
            j=j+1
    

    while i<len(left):

        arr[k]=left[i]
        i=i+1
        k=k+1

    while j<len(right):

        arr[k]=right[j]
        j=j+1
        k=k+1
    

    

        







def mergeSort(arr,l,r):
    if r>l:
        m=(r+l)//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)




arr=[10,5,30,15,7]


mergeSort(arr,0,4)

print(arr)