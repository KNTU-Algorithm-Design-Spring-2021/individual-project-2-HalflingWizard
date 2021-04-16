"""
WordWrap algorithm:
Given a sequence of words, and a limit on the number of characters that can be put in one line (line width). Put line breaks in the given sequence such that the lines are printed neatly. 
- Mohammad Namvarpour (Halfling Wizard)
Student number: 9920354 

"""

INF = 999999999 # an arbitary number choosed to play as infinity

def dispSolution(s, n):
    """A utility function to print the solution

    Args:
        s (int[]): solution of word wrapping problem 
        n (int): number of the words in text

    Returns:
        int: number of the current line
    """
    k = 0
    if s[n] == 1:
        k = 1
    else:
        k = dispSolution(s, s[n] - 1) + 1
    print('Line number ', k, ': From word no. ', s[n], 'to ', n)
    return k
  
def solveWordWrap (l, n, M):
    """this function solves word wrapping problem.

    Args:
        l (int[]): each item in this list is the length of a word
        n (int): number of the words in the text
        M (int): maximum number of characters in a line
    """
  
    # define two square matrix extraSpace and lineCost of order (size + 1)
    extraSpace = [[0 for i in range(n + 1)] for i in range(n + 1)]
    lineCost  = [[0 for i in range(n + 1)] for i in range(n + 1)]
               
    # define two array totalCost and solution of size (size + 1)
    totalCost = [0 for i in range(n + 1)]
    solution  = [0 for i in range(n + 1)]
      

    for i in range(n + 1): # find extra space for all lines
        extraSpace[i][i] = M - l[i - 1]
        for j in range(i + 1, n + 1): # extra space when word i to j are in single line
            extraSpace[i][j] = (extraSpace[i][j - 1] - l[j - 1] - 1)
                                      
 
    for i in range(n + 1): # find line cost for previously created extra spaces array
        for j in range(i, n + 1):
            if extraSpace[i][j] < 0:
                lineCost [i][j] = INF
            elif j == n and extraSpace[i][j] >= 0:
                lineCost [i][j] = 0
            else:
                lineCost [i][j] = (extraSpace[i][j] ** 3)
  
    totalCost[0] = 0
    for j in range(1, n + 1): # find minimum cost for words
        totalCost[j] = INF
        for i in range(1, j + 1):
            if (totalCost[i - 1] != INF and 
                lineCost [i][j] != INF and 
                ((totalCost[i - 1] + lineCost [i][j]) < totalCost[j])):
                totalCost[j] = totalCost[i-1] + lineCost [i][j]
                solution [j] = i
    dispSolution(solution , n)
      

wordLenArr = [3, 2, 2, 5] # each item is the length of a word
n = len(wordLenArr) # number of the words in text
maxWidth = 6 # maximum characters in a line
solveWordWrap(wordLenArr, n, maxWidth)
