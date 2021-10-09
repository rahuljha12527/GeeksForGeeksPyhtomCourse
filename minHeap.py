class myMinHeap:
    def __init__(self):
        self.arr=[]

    def parent(self,i): 
        return (i-1)//2
    
    def lChild(self,i):
        return 2*i+1
    
    def  rChild(self,i):
        return 2*i+2
    def insert(self,x):
        arr=self.arr
        arr.append(x)
        i=len(arr)-1

        while i>0 and arr[self.parent(i)]>arr[i]:
            p=self.parent(i)
            arr[i],arr[p]=arr[p],arr[i]
            i=p
    

    def minHeapify(self,i):
        arr=self.arr
        lt=self.lChild(i)
        rt=self.rChild(i)

        smallest=i
        n=len(arr)

        if lt<n and arr[lt]<arr[smallest]:
            smallest=lt
        if rt<n and arr[rt]<arr[smallest]:
            smallest=rt
        if smallest!=i:
            arr[smallest],arr[i]=arr[i],arr[smallest]
            self.minHeapify(smallest)

