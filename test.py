from binarytree import BinaryTree
from bktree import BKTree
from redblacktree import RedBlackTree
from metrics import levenshtein_distance_DP
from metrics import levenshtein_distance_recursive

import pickle
import time

def test_binarytree():
    test_passed = True
    test_database = pickle.load( open( 'testdatabase.p', 'rb' ) )
    test_database = test_database['binarytree']

    keys = test_database['keys']
    result = test_database['result']

    BT = BinaryTree()
    for key in keys:
        BT.insert(key,None)

    nodes = []
    nodes.append(BT._root)
    nodes_checked = 0

    while len(nodes) > 0:
        node = nodes.pop()
        if not node is None:
            nodes_checked += 1
            nodes.append(node._left)
            nodes.append(node._right)
            target = result[node._key]
            if node._left is None:
                if not target['l'] is None:
                    test_passed = False
            else:
                if not node._left._key == target['l']:
                    test_passed = False
            if node._right is None:
                if not target['r'] is None:
                    test_passed = False
            else:
                if not node._right._key == target['r']:
                    test_passed = False

    BT = BinaryTree()
    BT.insert('1','a')
    BT.insert('1','b')
    BT.insert('1','c')

    if len(BT.get('1')) != 3:
        test_passed = False

    return test_passed

def test_bktree():
    test_passed = True

    test_database = pickle.load( open( 'testdatabase.p', 'rb' ) )
    test_database = test_database['bktree']

    keys = test_database['keys']
    result_target = test_database['result']
    query = test_database['query']

    BKT = BKTree(levenshtein_distance_DP)
    for key in keys:
        BKT.insert(key)

    result = BKT.get(query)

    for (word,distance) in result:
        encounter = 0
        for (word_target,distance_target) in result_target:
            if word == word_target:
                if not distance == distance_target:
                    test_passed = False
                encounter +=1
        if not encounter == 1:
            test_passed = False

    return test_passed

def test_redblacktree():
    test_passed = True
    test_database = pickle.load( open( 'testdatabase.p', 'rb' ) )
    test_database = test_database['redblacktree']

    keys = test_database['keys']
    result = test_database['result']

    RBT = RedBlackTree()
    for key in keys:
        RBT.insert(key,None)

    nodes = []
    nodes.append(RBT._root)
    nodes_checked = 0

    while len(nodes) > 0:
        node = nodes.pop()
        if not node is None:
            nodes_checked += 1
            nodes.append(node._left)
            nodes.append(node._right)
            target = result[node._key]
            if node._parent is None:
                if not target['p'] is None: 
                    test_passed = False
            else:
                if not node._parent._key == target['p']:
                    test_passed = False
            if node._left is None:
                if not target['l'] is None:
                    test_passed = False
            else:
                if not node._left._key == target['l']:
                    test_passed = False
            if node._right is None:
                if not target['r'] is None:
                    test_passed = False
            else:
                if not node._right._key == target['r']:
                    test_passed = False
            if not node._black == target['b']:
                test_passed = False

    RBT = RedBlackTree()
    RBT.insert('1','a')
    RBT.insert('1','b')
    RBT.insert('1','c')

    if len(RBT.get('1')) != 3:
        test_passed = False

    return test_passed

def test_levenshtein_distance_DP():
    return test_levenshtein(levenshtein_distance_DP)

def test_levenshtein_distance_recursive():
    return test_levenshtein(levenshtein_distance_recursive)

def test_levenshtein(fnc):
    test_passed = True
    test_database = pickle.load( open( 'testdatabase.p', 'rb' ) )
    test_database = test_database['levenshtein']

    strings1 = test_database['strings1']
    strings2 = test_database['strings2']
    distances = test_database['distances']
    N = test_database['N']

    for i in range(N):
        if distances[i] != fnc(strings1[i],strings2[i]):
            test_passed = False

    return test_passed


if __name__ == "__main__":
    print("test BST")
    print(test_binarytree())
    print("some verification")
    print(levenshtein_distance_DP("acclimate", "data"))
    print("testing RB tree")
    print(test_redblacktree())
    print("===== Testing bktree =====")
    print(test_bktree())

    # print("Testing metrics.py in test.py")
    # print("-----------------------------\n")
    #
    #
    # print("Testing metrics.py - levenshtein_distance_DP")
    # start = time.time()
    # print(test_levenshtein_distance_DP())
    # print("DP test took %.4f\n" % (time.time() - start))
    #
    # print("Testing metrics.py - levenshtein_distance_recursive")
    # start = time.time()
    # print(test_levenshtein_distance_recursive())
    # print("recursive test took %.4f\n" % (time.time() - start))