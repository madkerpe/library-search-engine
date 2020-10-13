from numpy import zeros


def levenshtein_distance_recursive(str1,str2):
    """function to compute Levenshtein distance in a recursive manner"""

    i = len(str1)
    j = len(str2)
    if min(i,j) == 0:
        return max(i,j)
    else:
        return min(levenshtein_distance_recursive(str1[:-1], str2) + 1,
                   levenshtein_distance_recursive(str1, str2[:-1]) + 1,
                   levenshtein_distance_recursive(str1[:-1], str2[:-1]) + 1 - (str1[-1:] == str2[-1:]))



def levenshtein_distance_DP(str1,str2):
    """function to compute Levenshtein distance in a DP manner with a full matrix"""
    
    #Bepalen van de dimenties van de matrix
    m = len(str1) + 1
    n = len(str2) + 1

    #Een matrix initialiseren, de subproblemen met strings met lengte 0 al ingevuld (complexiteit (m+1)*(n+1) )
    d_matrix = [[0 for x in range(m)] for y in range(n)]
    d_matrix[0] = [x for x in range(m)] 
    for y in range(n):
        d_matrix[y][0] = y


    #Itereren over matrix bottom-up en de matrix opvullen
    for y in range(1, n):
        for x in range(1, m):
            d_matrix[y][x] = min(d_matrix[y][x-1] + 1, d_matrix[y-1][x] + 1, d_matrix[y-1][x-1] + Indicator(str1[x-1], str2[y-1]))

    return d_matrix[n-1][m-1]

def levenshtein_distance_DP_less_memory(str1,str2):
    """function to compute Levenshtein distance in a DP manner with a full matrix"""
    m = len(str1) + 1
    n = len(str2) + 1

    #initialising a matrix, cases with strings of lenght 0 filled in (complexity (m+1)*(n+1))
    d_matrix = [[0 for x in range(m)] for y in range(2)]
    d_matrix[0] = [x for x in range(m)]

    for y in range(1, n):
        for x in range(1, m):
            d_matrix[y%2][0] = y
            d_matrix[y%2][x] = min(d_matrix[y%2][x-1] + 1, d_matrix[(y-1)%2][x] + 1, d_matrix[(y-1)%2][x-1] + Indicator(str1[x-1], str2[y-1]))

    return d_matrix[(n-1)%2][m-1]

def Indicator(a, b):
    """return 0 if a == b, return 1 if not"""
    return 1*(a!=b)



if __name__ == "__main__":
    # print("Testing metrics.py - levenshtein_distance_recursive")
    # print(str(levenshtein_distance_recursive("kitten", "sitting")) + " should be 3")
    # print(str(levenshtein_distance_recursive("algorithm", "algorith")) + " should be 1")
    # print(str(levenshtein_distance_recursive("algorithm", "algoritho")) + " should be 1")
    # print(str(levenshtein_distance_recursive("algorithm", "algoritmh")) + " should be 2")
    
    print("Testing metrics.py - levenshtein_distance_DP")

    def print_matrix(matrix):
        """pretty print function for printing nested lists (debug function)"""
        dash = '-'
        line = dash*3*len(matrix[0])

        print(line)
        for i in range(len(matrix)):
            print(matrix[i])

        print(line)

    def test_levenshtein_DP(str1, str2, correct_value):
        """test the DP version of the levenshtein metric (debug function)"""
        res = levenshtein_distance_DP_less_memory(str1, str2)
        if (res == correct_value):
            passed = "Test passed"
        else:
            passed = "Test didn't pass"

        print("result = %d, %s" % (res, passed))


    test_levenshtein_DP("ten", "tent", 1)
    test_levenshtein_DP("algorithm", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", 1)
    test_levenshtein_DP("algorithm", "algoritho", 1)
    test_levenshtein_DP("algorithm", "algoritmh", 2)
    test_levenshtein_DP("saturday", "sunday", 3)
    test_levenshtein_DP("algorithm", "acclimate", 8)
    test_levenshtein_DP("algorithm", "acclaim", 6)