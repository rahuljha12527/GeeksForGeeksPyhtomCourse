def printNos(self,N):
        if(N>0):#The loop runs till N>1
            self.printNos(N-1)#We keep on recursing till the end as we want to print from 1 to N
            print(N,end=" ")#When recursion is done then print N