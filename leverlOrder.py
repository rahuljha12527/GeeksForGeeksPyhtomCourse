class Node:
    def __init__(self,k):
        self.left=None
        self.right=None
        self.key=k


def printLevelOrder(root):
    if root is None:
        return
    st=[root]

    while len(st)>0:
        curr=st.pop()
        print(curr.key)


        if curr.left is not None:
            st.append(curr.left)
        if curr.right is not None:
            st.append(curr.right)


# Driver Code
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)

printLevelOrder(root)