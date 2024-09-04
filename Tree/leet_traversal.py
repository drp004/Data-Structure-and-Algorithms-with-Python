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

    def inorder(self, root):
        def traversal(root, lst):
            if root:
                traversal(root.left, lst)
                lst.append(root.data)
                traversal(root.right, lst)

        lst = []
        traversal(root, lst)
        return lst    

    def inorder2(self, root):
        if root:
            self.inorder2(root.left)
            print(root.data, end=" ")
            self.inorder2(root.right) 

if __name__ == "__main__":
    lst = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, 7, -1, -1, -1]
    tree = Tree()
    root = tree.create(lst)  
    ls = tree.inorder(root)
    print(ls)
    tree.inorder2(root)