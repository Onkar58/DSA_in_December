def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
    l = len(original)
    if m*n == l:
        k = 0
        arr = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                arr[i][j] = original[k]
                k += 1
        return arr
    else:
        return []
        
array = [1,2,3,4]
construct2DArray(array, 2, 2)
