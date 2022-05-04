def solution(S):
    n = len(S)
  
    
    L = [[0 for x in range(n)]for y in range(n)]
  
   
    for i in range(n):
        L[i][i] = 1
  
    
    for cl in range( 2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if (S[i] == S[j] and cl == 2):
                L[i][j] = 2
            elif (S[i] == S[j]):
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1],L[i + 1][j])
  
    
    return L[0][n - 1]
  

def minimumNumberOfDeletions( S):
 
    n = len(S)

  
    
    l = solution(S)
  
    
    return (n - l)
  
# Driver Code
if __name__ == "__main__":
     
    S = "X"
    print( "Minimum number of deletions = "
         , minimumNumberOfDeletions(S))