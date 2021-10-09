def insert(root,key):
    parent=None
    curr=root
    while curr!=None:
        parent=curr
        if curr.key==key:
            return root
        elif curr.key<key:
            curr=curr.left
        else:
            curr=curr.right
    
    if parent==None:
        return Node(key)
    if parent.key>key:
        parent.left=Node(key)
    else:
        parent.right=Node(key)

    return root