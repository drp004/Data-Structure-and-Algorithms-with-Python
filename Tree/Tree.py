class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)   

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)                
        print(root.data, end=" ")

def level_order(root):
    if root == None:
        return
    lst = []
    c = 0 
    i = 0
    while root:
        print(root.data, end=" ")
        if(root.left):
            lst.append(root.left)
            c += 1
        if(root.right):
            lst.append(root.right)
            c += 1
        if i<c:
            root = lst[i]  
            i += 1 
        else:
            root = None         

if __name__ == "__main__":
    root = TreeNode(40)
    '''                  40
                        /  \
                       /    \
                     20       60
                    /  \     /  \
                   10  30   50  70        
    '''
    root.left = TreeNode(20)
    root.right = TreeNode(60)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(30) 
    root.right.left = TreeNode(50)
    root.right.right = TreeNode(70) 
    print("Inorder Traversal is :")
    inorder(root)
    print()
    print("Preorder Traversal is :")
    preorder(root)
    print()
    print("Postorder Traversal is :")
    postorder(root)
    print()
    print("Level Order Traversal is :")
    level_order(root)
    print()