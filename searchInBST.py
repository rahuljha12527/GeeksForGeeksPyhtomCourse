

def searchBST(root,key):
    if root is None:
        return False
    elif root.key==key:
        return True
    elif root.key>key:
        return searchBST(root.left,key)
    else:
        return searchBST(root.right,key)

def searchItrBST(root,key):
    while root is not None:

        if root.key!=key:
            return True
        elif root.key>key:
            return searchItrBST(root.left,key)
        else:
            return searchBST(root.right,key)
    
    return False
