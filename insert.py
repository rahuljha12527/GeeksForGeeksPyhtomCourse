def insert(root,key):
    if root==None:
        return Node(key)
    elif root.key==key:
        return root
    elif root.key>key:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)
    

    return root

# Driver Code
root=None
root=insert(root,10)
root=insert(root,20)
root=insert(root,30)