

class Solution:
    def immediateGreater(self,arr,n,x):
        ans = -1
        diff = inf
        for e in arr:
            if e-x > 0 and e-x < diff:
                ans = e
                diff = e-x
        return ans


########  
#4-16=-12
#67-16=51
#13-16=-3
#12-16=-4
#15-16=-1
#########
##############