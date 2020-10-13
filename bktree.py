class BKTreeNode():
    """represents a node of the tree. """
    
    def __init__(self, key):
        self._key = key
        self._children = {}

    def contains(self, item):
        for node in self._children:
            if node._key == item:
                return True
        return False

    def get(self, dist):
        for node in self._children:
            if node._key == dist:
                return node

    def add_child(self, key):
        self._children[key] = BKTreeNode(key)

class BKTree():
    """implement the “insert” and “get” method for a BK-tree. 
    Only keys are stored in the BK-tree. 
    The “get” method returns all words at a maximum distance of “max_dist” to the provided key.
    """

    def __init__(self, distance_function):
        self._root = None
        self._count = 0
        self._distance_function = distance_function
        
    def __len__(self):
        return self._count
        
    def insert(self, key):
        """complete this function"""
        if self._root is None:
            self._root = BKTreeNode(key)
        else:
            added_child = False
            current_node = self._root
            while not added_child:
                distance = self._distance_function(key,current_node._key)
                if distance in current_node._children:
                    current_node = current_node._children[distance]
                else:
                    current_node._children[distance] = BKTreeNode(key)
                    added_child = True
            self._count += 1

    def get(self, key, max_dist = 1):
        results = []
        pot_nodes = [self._root]
        while len(pot_nodes) != 0:
            current_node = pot_nodes[0]
            dist = self._distance_function(key, current_node._key)
            for child_key in current_node._children:
                if dist-max_dist <= child_key <= dist+max_dist:
                    if self._distance_function(current_node._children[child_key]._key, key) <= max_dist:
                        results.append(current_node._children[child_key]._key)
                    pot_nodes.append(current_node._children[child_key])
            pot_nodes.pop(0)
        return results



if __name__ == "__main__":
    print("Testing bktree.py")