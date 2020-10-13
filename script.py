from project import QueryProcessor
from project import Dataset
from ranker import Ranker
from binarytree import BinaryTree
from redblacktree import RedBlackTree
from bktree import BKTree
from metrics import levenshtein_distance_DP
import pickle

import nltk
nltk.download('stopwords')

DEBUG_MODE = False            #Loads a pickle-files instead of generating the big data-structures again
CONSTRUCT_DEBUG_MODE = False    #Constructs pickle-files for the big data-structures

"""Provide a script where you load the dataset, process it into an efficient binary search tree, 
    create a BK-tree and finally create a Ranker. Get the book-titles for “The search engine.”

	This should only be a couple of lines as all algorithms should be implemented in the other files. 
    It demonstrates a fully working setup
"""

query_processor = QueryProcessor()

if DEBUG_MODE:
    dataset = pickle.load(open("dataset.p", 'rb'))
    print("Dataset Loaded!")

    binary_search_tree = pickle.load(open("binary_search_tree.p", 'rb'))
    print("RB-Tree constructed!")

    bk_tree = pickle.load(open("bk_tree.p", 'rb'))
    print("BK Tree constructed!")


else:
    csv_file = "Brooklyn_Public_Library_Catalog.csv"

    #Provide a script where you load the dataset
    print("Constructing dataset........", end='', flush=True)
    dataset = Dataset(csv_file, query_processor)
    dataset.load()
    print("Dataset Loaded!")

    #process it into an efficient binary search tree
    print("Constructing RB-Tree...", end='', flush=True)
    binary_search_tree = RedBlackTree()
    temp_dataset = dataset.get_token_bookids()
    for i in range(len(temp_dataset)):
        binary_search_tree.insert(temp_dataset[i][0], temp_dataset[i][1])
    print("RB-Tree constructed!")

    #create a BK-tree
    print("Constructing BK-Tree...", end='', flush=True)
    bk_tree = BKTree(levenshtein_distance_DP)
    english_dictionary_list = dataset.get_dictionary()
    for i in range(len(english_dictionary_list)):
        bk_tree.insert(english_dictionary_list[i])
    print("BK-Tree constructed!")


    if CONSTRUCT_DEBUG_MODE:
        pickle.dump(dataset, open("dataset.p", 'wb'))
        pickle.dump(binary_search_tree, open("binary_search_tree.p", 'wb'))
        pickle.dump(bk_tree, open("bk_tree.p", 'wb'))

#create a Ranker
ranker = Ranker(dataset, query_processor, binary_search_tree, bk_tree)

#Get the book-titles for “The search engine.”
ranker.evaluate("The search engine.")
