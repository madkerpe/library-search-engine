class Ranker():
    """implement the “evaluate” method. 
    This method gets a query, processes the query and retrieves book_ids using an efficient binary search tree. 
    If for a specific token in the query less than 5 results are available from the binary search tree, 
    the original word is processed with a BK-tree to get similar words up to a distance of 2. 
    For these words, additional results are retrieved from the binary search tree. 
    Each match of a token/word with a title represents one point for that title. 
    In the end, the function returns the titles with the highest scores (sort using python method). 
    Pay specific attention to the Python data structure you will use to store temporary scores during this operation!
    """

    def __init__(self,dataset,query_processor,binary_search_tree,bk_tree = None, amount_of_results_shown=10):
        self._dataset = dataset
        self._query_processor = query_processor
        self._binary_search_tree = binary_search_tree
        self._bk_tree = bk_tree
        self.amount_of_results_shown = amount_of_results_shown


    def evaluate(self,query):
        #This method gets a query, processes the query
        processed_querry = self._query_processor.process(query, stem=True)
        matches_count = {}
        did_you_mean = ""
        slash = "/"
        
        #retrieves book_ids using an efficient binary search tree.
        for reduced_word in processed_querry:
            #ik ga ervanuit dat dit een lijst met book_id's teruggeeft
            matched_book_ids = self._binary_search_tree.get(reduced_word)

            if matched_book_ids == None:
                matched_book_ids = []

            else:
                pass
            
            #If for a specific token in the query less than 5 results are available from the binary search tree
            if len(matched_book_ids) < 5:
                corrected_word_list = list(set(self._bk_tree.get(reduced_word, 2)))
                did_you_mean += slash.join(corrected_word_list) + " "

                #If for a specific token in the query less than 5 results are available from the binary search tree
                #the original word is processed with a BK-tree, get similar words up to a distance of 2
                for corrected_word in corrected_word_list:
                    
                    corrected_matched_book_ids = self._binary_search_tree.get(corrected_word)
                    if corrected_matched_book_ids != None:
                        matched_book_ids += corrected_matched_book_ids
                        

            else:
                did_you_mean += reduced_word + " "

            for book_id in matched_book_ids:
                if book_id in matches_count:
                    #Each match of a token/word with a title represents one point for that title
                    matches_count[book_id] = matches_count[book_id] + 1

                else:
                    matches_count[book_id] = 1            


        #Generating console output
        print("  _   _            _          _ ")
        print(" | | | | ___   ___| |__   ___| |")
        print(" | |_| |/ _ \ / _ \ '_ \ / _ \ |")
        print(" |  _  | (_) |  __/ | | |  __/ |")
        print(" |_| |_|\___/ \___|_| |_|\___|_|")
        print("                                ")
        print("Did you mean: %s" % did_you_mean)
        print("                                ")
        
        counter = 0
        for pair in sorted(matches_count.items(), key=lambda x: x[1], reverse=True):
            
            print("page-rank=%d hit-counter=%d book-id=%d" % (counter + 1, pair[1], pair[0]))
            
            try: 
                print("  %s" % self._dataset.get_title(pair[0]))
            except UnicodeEncodeError:
                print("<Python had a hard time printing this title>")
            print("--------------------------------")
            
            counter += 1
            if counter >= self.amount_of_results_shown:
                break
