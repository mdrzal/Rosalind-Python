import numpy as np
#insert your sample data
s="AAAACCCGGT"
s=np.asarray(list(s))

a=s=="A"
t=s=="T"
c=s=="C"
g=s=="G"

s[a]="T"
s[t]="A"
s[g]="C"
s[c]="G"

#output data
print("".join(s)[::-1])
