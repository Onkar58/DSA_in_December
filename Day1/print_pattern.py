def printPat(n):
    word = str()
      for i in range(n, 0, -1):
          for j in range(n,0,-1):
              y = str(j)
              word +=((y+' ')*i)
              # print((str(j)+" ")*i, end="")  
          # print("$", end="")
          word += '$'
      print(word)
printPat(5)

"""Prints Pattern like
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1 
in the form of 
3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1
"""
