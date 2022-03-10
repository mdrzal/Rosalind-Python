from collections import Counter
#insert the strin as s
s="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
s=Counter(list(s))
print(s["A"],s["C"],s["G"],s["T"])
