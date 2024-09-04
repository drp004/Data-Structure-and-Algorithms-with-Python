class Treenode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def insert_node(root, data):
    if root == None:
        return Treenode(data)
    else:
        if data == root.data:
            return root
        elif(data < root.data):
            root.left = insert_node(root.left, data)
        else:
            root.right = insert_node(root.right, data) 
    return root    

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)    

def heightOftree(root):
    if root == None :
        return 0

    l =  heightOftree(root.left) 
    r =  heightOftree(root.right) 
        
    return max(l, r) + 1

def ArrayToBST(lst):
    if len(lst) == 0:
        return None

    mid = len(lst)//2    
    
    return Treenode(lst[mid], ArrayToBST(lst[:mid]), ArrayToBST(lst[mid+1:]))

if __name__ == "__main__":
    root = None
    root = insert_node(root, 40)
    root = insert_node(root, 20)
    root = insert_node(root, 60)
    root = insert_node(root, 10)
    root = insert_node(root, 30)
    root = insert_node(root, 50)
    root = insert_node(root, 70)
    root = insert_node(root, 5)
    print("Inorder Traversal is :")
    inorder(root)
    print("\nheight of node is :", heightOftree(root))
    lst = [5, 10, 20, 30, 40, 50, 60, 70]
    r2 = ArrayToBST(lst)
    print("Inorder Traversal of Tree2 is :")
    inorder(r2)