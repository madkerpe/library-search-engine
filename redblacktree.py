class RedBlackTreeNode():
    
    """represents a node of the tree. Leaf nodes are represented by None.
    You can add to this class.
    """
    def __init__(self, key, value, parent = None, left = None, right = None, black = False):
        self._key = key
        self._values = [value]
        self._parent = parent
        self._black = black
        self._left = left
        self._right = right

    def other_child(self, node):
        if node == self._left:
            return self._right
        elif node == self._right:
            return self._left
        else:
            print("ERROR: node should be child of parent, redblacktree.py, other_child()")
            return None

    def uncle(self):
        if self._parent is not None:
            if self._parent._parent is not None:
                return self._parent._parent.other_child(self._parent)

    def is_right_black(self):
        if self._right is None:
            return True
        else:
            return self._right._black

    def set_black(self):
        self._black = True


    def set_red(self):
        self._black = False


    def is_left_black(self):
        if self._left is None:
            return True
        else:
            return self._left._black


    def is_parent_black(self):
        if self._parent is None:
            return True
        else:
            return self._parent._black

    def recolor(self):
        self._black = not self._black

    def grandparent(self):
        return self._parent._parent

    def is_triangle(self):
        if self._parent is not None:
            if self == self._parent._left:
                if self.grandparent() is not None:
                    return self.grandparent()._right == self._parent
                else:
                    return False
            else:
                if self.grandparent() is not None:
                    return self.grandparent()._left == self._parent
                else:
                    return False
        else:
            return False

    def is_line(self):
        if self._parent is not None:
            if self.grandparent() is not None:
                return ((self.grandparent()._left == self._parent and self._parent._left is self)
                        or (self.grandparent()._right == self._parent and self._parent._right is self))
            else:
                return False
        return False

    def is_left_child(self,parent):
        if parent is not None:
            return self == parent._left
        return False

    def is_right_child(self,parent):
        if parent is not None:
            return self == parent._right
        return False

    def get(self, key):
        if key == self._key:
            return self._values
        elif key < self._key:
            #go to left
            if self._left is not None:
                return self._left.get(key)
            else:
                return None
        else:
            #to to right
            if self._right is not None:
                return self._rigth.get(key)
            else:
                return None



class RedBlackTree():
    """implement the “insert”, “get”, “_right_rotate“ and “_left_rotate” methods 
    for a red-black tree which stores data within the nodes. The operation is similar to the binary tree. 
    Other binary tree methods (e.g. delete) do not have to be implemented. 
    """
    
    def __init__(self):
        self._root = None
        self._count = 0
        
    def __len__(self):
        return self._count

    def insert(self, key, value):
        if self._root is None:
            self._root = RedBlackTreeNode(key, value, black=True)
        else:
            add_el = False
            local_root = self._root
            while not add_el:
                if local_root._key == key:
                    local_root._values.append(value)
                    add_el = True
                elif local_root._key < key:
                    #to the right
                    if local_root._right is not None:
                        local_root = local_root._right
                    else:
                        local_root._right = RedBlackTreeNode(key, value)
                        local_root._right._parent = local_root
                        self.check_properties(local_root._right)
                        add_el = True
                else:
                    #to the left
                    if local_root._left is not None:
                        local_root = local_root._left
                    else:
                        local_root._left = RedBlackTreeNode(key, value)
                        local_root._left._parent = local_root
                        self.check_properties(local_root._left)
                        add_el = True
        self._count += 1

    def check_properties(self, node):
        z = node
        while z._parent is not None and not z._parent._black:
            if z._parent == z.grandparent()._left:
                y = z.grandparent()._right
                if y is not None and not y._black:
                    z._parent.set_black()
                    y.set_black()
                    z.grandparent().set_red()
                    z = z.grandparent()
                elif z == z._parent._right:
                    z = z._parent
                    self._left_rotate(z)
                else:
                    z._parent.set_black()
                    z.grandparent().set_red()
                    self._right_rotate(z.grandparent())
            else:
                y = z.grandparent()._left
                if y is not None and not y._black:
                    z._parent.set_black()
                    y.set_black()
                    z.grandparent().set_red()
                    z = z.grandparent()
                elif z == z._parent._left:
                    z = z._parent
                    self._right_rotate(z)
                else:
                    z._parent.set_black()
                    z.grandparent().set_red()
                    self._left_rotate(z.grandparent())
        self._root._black = True


    def recheck_root(self):
        while self._root._parent is not None:
            self._root = self._root._parent


                            
    def _right_rotate(self, node):
        x = node
        y = x._left
        x._left = y._right
        if y._right is not None:
            y._right._parent = x
        y._parent = x._parent
        if x._parent is None:
            self._root = y
        elif x == x._parent._right:
            x._parent._right = y
        else:
            x._parent._left = y
        y._right = x
        x._parent = y

        
    def _left_rotate(self, node):
        x = node
        if x._right is not None:
            y = x._right
            x._right = y._left

            if y._left is not None:
                y._left._parent = node

            y._parent = x._parent

            if x._parent is None:
                self._root = y
            elif x == x._parent._left:
                x._parent._left = y
            else:
                x._parent._right = y

            y._left = x
            x._parent = y
                    
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
    print("Testing redblacktree.py")
    
    #test right rotate
    A = RedBlackTreeNode("A", 1)
    B = RedBlackTreeNode("B", 1)
    C = RedBlackTreeNode("C", 1)

    P = RedBlackTreeNode("P", 1, left=A, right=B)
    A._parent = P
    B._parent = P

    Q = RedBlackTreeNode("Q", 1, left=P, right=C)
    P._parent = Q
    C._parent = Q

    Root = RedBlackTree()

    Root._right_rotate(Q)
    Root._left_rotate(P)


    test_array = [9,12,19,20,1,7,11,5,8,6,17,2,13,3,16,15,18,4,10,14]
    #test_array = [9,4,1]
    max_test_length = 20
    #test insert with rot
    tree = RedBlackTree()
    for i in range(max_test_length):
        tree.insert(test_array[i], str(test_array[i]))
    print(len(tree))
    a = 5
