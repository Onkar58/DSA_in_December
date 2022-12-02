def sumOddLengthSubarrays(arr: List[int]) -> int:
    n = len(arr)
    ans = 0
    for i in range(n):
        ans += ((i+1)*(n-i) + 1)//2 * arr[i]
    print(ans)
    return ans

a = [1,2,3,4,5]
sumOddLengthSubarrays(a)
