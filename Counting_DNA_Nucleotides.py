from collections import Counter
s="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
s=Counter(list(s))
print(s["A"],s["C"],s["G"],s["T"])
