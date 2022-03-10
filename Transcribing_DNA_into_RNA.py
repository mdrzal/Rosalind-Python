import numpy as np
#paste your DNA string below
s="GATGGAACTTGACTACGTAAATT"
s=np.asarray(list(s))
s[s=="T"]="U"
print("".join(s)) #This will be the RNA string
