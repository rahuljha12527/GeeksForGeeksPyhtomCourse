#Function to find the preorder traversal of the tree.
def preorderUtil(root, res):
    #preorder traversal works on Root Left Right.
    
    #if root is null then we simply return. 
    if root is None: 
        return
    
    #first, we store the data at root in a list.
    res.append (root.data)
    #then we call the recursive function for left subtree.
    preorderUtil(root.left, res)
    #then we call the recursive function for right subtree.
    preorderUtil(root.right, res)
    

#Function to return a list containing the preorder traversal of the tree.    
def preorder (root):
    res = []
    preorderUtil (root, res)
    #returning the list.
    return res