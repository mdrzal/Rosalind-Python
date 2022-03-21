in_string="""GATATATGCATATACTT
ATAT"""

A=in_string.split('\n')

s=A[0]
s1=A[1]

A1=list()
for i in range(len(s)):
    if s[i:].startswith(f"{s1}"):
        keep=str(i+1)
        A1.append(keep)
        
print(" ".join(A1))
