def power(self,N,R):
    """Function returns the number raised to its reverse and modulous of 1000000007"""
    res = 1
    while(R>0):
          if R%2==1:
              res = (res*N)%1000000007
        R = R//2
        N = (N * N)%1000000007
    return res        
      
print(power(2, 2))
