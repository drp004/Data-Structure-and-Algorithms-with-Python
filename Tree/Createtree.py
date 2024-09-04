class Treenode:
    def __init__(self,data=None):
        self.data = data    
        self.left = None
        self.right = None

class Tree:

    ind = -1

    def create(self,lst):
        self.ind += 1
        if lst[self.ind] == -1 :
            return None

        new = Treenode(lst[self.ind])
        new.left = self.create(lst)
        new.right = self.create(lst)

        return new

    def preorder(self,root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
            return

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)   

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)                
            print(root.data, end=" ")

    def level_order(self, root):
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

    def countNode(self, root):
        if root == None:
            return 0

        letftree = self.countNode(root.left)
        righttree = self.countNode(root.right)

        return letftree + righttree + 1
    
    def sumOfNode(self, root):
        if root == None:
            return 0

        letftree =  self.sumOfNode(root.left)
        righttree =  self.sumOfNode(root.right)
        
        return letftree + righttree + root.data   

    def heightOftree(self, root):
        if root == None :
            return 0

        letftree =  self.heightOftree(root.left) 
        righttree =  self.heightOftree(root.right) 
        
        if letftree>righttree:
            height = letftree + 1
        else:
            height = righttree + 1   

        return height     

if __name__ == "__main__":
    lst = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, 7, -1, -1, -1]
    tree = Tree()
    root = tree.create(lst)  
    print("Preorder Traversal is :")               
    tree.preorder(root)
    print("\nInorder Traversal is :")
    tree.inorder(root)
    print("\nPostorder Traversal is :")
    tree.postorder(root)
    print("\nLevelorder Traversal is :")
    tree.level_order(root)
    print("\nNumber of node is :", tree.countNode(root))
    print("Sum of node is :", tree.sumOfNode(root))
    print("height of node is :", tree.heightOftree(root))
