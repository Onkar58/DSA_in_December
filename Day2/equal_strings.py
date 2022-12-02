def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    n1 = len(word1)
    n2= len(word2)
    str1 = ""
    str2 = ""
    for i in range(n1):
        str1 += word1[i]
    for j in range(n2):
        str2 += word2[j]
    if str1==str2:
        return True
    else:
        return False
    
a1 = ["ab", "c"]
a2 = ["a", "bc"]
print(arrayStringAreEqual(a1, a2))
