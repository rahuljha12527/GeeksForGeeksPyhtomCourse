class Node:
    def __init__(self,key):
        self.left=None
        self.key=key
        self.right=None
def getFloor(root,x):
    res=None

    while root!=None:
        if root.key==x:
            return root
        elif root.key>key:
            root=root.left
        else:
            res=root
            root=root.right
    

    return res      