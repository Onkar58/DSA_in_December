def nthFibonacci(self, n):
    """Returns the nth fibonacci number its modulous of 100000007"""
    n1 = 0
    n2 = 1
    n3 = n1+n2
    if n == 1:
        return n1
    elif n == 2 or n == 3:
        return n2
    else:
        for i in range(n-2):
            n1 = n2
            n2 = n3
            n3 = n1 + n2
    return n3%1000000007
