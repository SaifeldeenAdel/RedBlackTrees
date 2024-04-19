from TreeNode import TreeNode


class RBTree:
    def __init__(self):
        self.null = TreeNode(0)
        self.root = self.null

    def insert(self, value):
        newNode = TreeNode(value)
        newNode.parent = None
        newNode.left = self.null
        newNode.right = self.null
        newNode.red = True

        parent = None
        current = self.root

        # Getting position of new node's parent
        while current != self.null:
            parent = current
            if newNode.value < current.value:
                current = current.left
            elif newNode.value > current.value:
                current = current.right
            else:
                print("ERROR: Word already in the dictionary!")
                return

        # Setting parent and inserting new node
        newNode.parent = parent
        if parent == None:
            self.root = newNode
        elif newNode.value < parent.value:
            parent.left = newNode
        else:
            parent.right = newNode

        self.fixInsert(newNode)

    def leftRotate(self, a):
        b = a.right
        a.right = b.left
        if b.left != self.null:
            b.left.parent = a

        b.parent = a.parent
        if a.parent == None:
            self.root = b
        elif a == a.parent.left:
            a.parent.left = b
        else:
            a.parent.right = b
        b.left = a
        a.parent = b

    def rotateRight(self, a):
        b = a.left
        a.left = b.right
        if b.right != self.null:
            b.right.parent = a

        b.parent = a.parent
        if a.parent == None:
            self.root = b
        elif a == a.parent.right:
            a.parent.right = b
        else:
            a.parent.left = b
        b.right = a
        a.parent = b

    def fixInsert(self, newNode):
        while newNode != self.root and newNode.parent.red:
            if newNode.parent == newNode.parent.parent.right:
                u = newNode.parent.parent.left
                if u.red:
                    # Perform color flip if uncle is red
                    u.red = False
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    newNode = newNode.parent.parent
                else:
                    # Perform rotations if uncle is black
                    if newNode == newNode.parent.left:
                        newNode = newNode.parent
                        self.rotateRight(newNode)
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    self.leftRotate(newNode.parent.parent)
            else:
                u = newNode.parent.parent.right
                if u.red:
                    # Perform color flip if uncle is red
                    u.red = False
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    newNode = newNode.parent.parent
                else:
                    # Perform rotations if uncle is black
                    if newNode == newNode.parent.right:
                        newNode = newNode.parent
                        self.leftRotate(newNode)
                    newNode.parent.red = False
                    newNode.parent.parent.red = True
                    self.rotateRight(newNode.parent.parent)
        self.root.red = False

    def searchTree(self, value):
        current = self.root
        while current != self.null:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                print(f"Found in tree!")
                return current
        print("Element not in tree")
        return None

    def getBlackHeight(self):
        # Just go down the tree till we hit a null, counting black nodes
        current = self.root
        count = 0
        while current != self.null:
            if not current.red:
                count += 1
            current = current.left
        return count

    def getTreeHeight(self, root):
        if self.root == None:
            return 0
        else:
            left = 0
            right = 0

            if root.left != None and root.left != self.null:
                left = self.getTreeHeight(root.left)
            if root.right != None and root.right != self.null:
                right = self.getTreeHeight(root.right)

            maximum = left if (left > right) else right

        return maximum + 1

    def getTreeSize(self, root):
        if self.root == None:
            return 0
        else:
            countLeft = 0
            countRight = 0

            if root.left != None and root.left != self.null:
                countLeft = self.getTreeSize(root.left)
            if root.right != None and root.right != self.null:
                countRight = self.getTreeSize(root.right)

        return countLeft + countRight + 1

    def printTreeRec(self, root, space):
        # Base case
        if root == None:
            return

        space += 5
        # Process right child
        self.printTreeRec(root.right, space)

        print()
        for i in range(5, space):
            print(end=" ")
        print(f"{root.value}{'-r' if root.red else '-b'}")

        # Process left child
        self.printTreeRec(root.left, space)

    def printTree(self):
        self.printTreeRec(self.root, 0)

    def printInfo(self):
        print(f"Tree Height: {self.getTreeHeight(self.root)}")
        print(f"Black Height: {self.getBlackHeight()}")
        print(f"Tree Size: {self.getTreeSize(self.root)}")


def main():
    tree = RBTree()
    for x in range(1, 5):
        n = input("Enter: ")
        tree.insert(n)
        tree.printInfo()
    tree.printTree()


if __name__ == "__main__":
    main()
