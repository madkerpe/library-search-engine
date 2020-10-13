class BinaryTreeNode():
    """represents a node of the tree. Leaf nodes 
    are represented by None. You can add to this class."""
    
    def __init__(self, key, value, left=None, right=None):
        self._key = key
        self._values = [value]
        self._left = left
        self._right = right

    def insert(self, key, value):
        if self._key > key:
            # insert on the left
            if self._left is not None:
                self._left.insert(key, value)
            else:
                self._left = BinaryTreeNode(key, value)
        elif self._key < key:
            # insert on the right
            if self._right is not None:
                self._right.insert(key, value)
            else:
                self._right = BinaryTreeNode(key, value)
        else:
            # same key, add to value
            self._values.append(value)

    def get(self, key):
        if self._key == key:
            return self._values
        elif self._key > key:
            #should be on the left
            if self._left is not None:
                return self._left.get(key)
            else:
                return None
        else:
            #should be on the right
            if self._right is not None:
                return self._right.get(key)
            else:
                return None


class BinaryTree():
    """implement the “insert” and “get” methods for a binary tree which stores data within the nodes. 
    The “insert” method inserts a book_id (value) into the tree for a specific token (key). 
    Note: if a key already exists, the values should be appended to a List. 
    Make sure to update the _count variable representing the number of nodes in the tree. 
    Other binary tree methods (e.g. delete) do not have to 	be implemented. 
    """
    
    def __init__(self):
        self._root = None
        self._count = 0


    def __len__(self):
        return self._count


    def insert(self, key, value):
        self._count += 1
        if self._count%1000 == 0:
            print("at: " + str(self._count))
        if self._root is None:
            self._root = BinaryTreeNode(key, value)
        else:
            current_node = self._root
            found = False
            while not found:
                if key < current_node._key:
                    if current_node._left is not None:
                        current_node = current_node._left
                    else:
                        current_node._left = BinaryTreeNode(key, value)
                        found = True
                elif key > current_node._key:
                    if current_node._right is not None:
                        current_node = current_node._right
                    else:
                        current_node._right = BinaryTreeNode(key, value)
                        found = True
                else:
                    current_node._values.append(value)
                    found = True


    def get(self, key):
        if self._root is not None:
            node = self._root
            while node is not None:
                if node._key == key:
                    return node._values
                if node._key > key:
                    node = node._left
                else:
                    node = node._right
        else:
            return None



if __name__ == "__main__":
    print("Testing binarytree.py")
    root = BinaryTree()

    root.insert(8, "West Vlaams voor dummies")
    root.insert(4, "Waarom Gistel een wereldstad is")
    root.insert(7, "g en h wat is het verschil")
    root.insert(7, "weglaten die klanken")
    root.insert(10, "hitgub voor dummies")
    root.insert(2, "Het leven aan de zee")

    print(root.get(8))
    print(root.get(4))
    print(root.get(7))
    print(root.get(10))
    print(root.get(2))

    #add breakpoint
    a = 5