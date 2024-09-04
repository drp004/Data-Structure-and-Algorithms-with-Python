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

def PathSum(root, targetSum):
    if root == None:
        return False

    if root.left == None and root.right == None:
        return targetSum == root.data

    left_sum = PathSum(root.left, targetSum - root.data)              
    right_sum = PathSum(root.right, targetSum - root.data)

    return left_sum or right_sum              

if __name__ == "__main__":
    root = None
    root = insert_node(root, 40)
    root = insert_node(root, 20)
    root = insert_node(root, 60)
    root = insert_node(root, 10)
    root = insert_node(root, 30)
    root = insert_node(root, 50)
    root = insert_node(root, 70)
    print("Inorder Traversal is :")
    inorder(root)
    print()
    print("Sum 90 is there ? ", PathSum(root, 90))
    print("Sum 110 is there ? ", PathSum(root, 110))