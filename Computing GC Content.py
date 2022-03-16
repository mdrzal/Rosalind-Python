import re
import pandas as pd
import numpy as np

A=""">Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

A=A.split("\n")
A1=list()
for i in A:
     A1.append(bool(re.match("^>Rosalind", i)))

A1.append(True)

l=len(A)
s=list()
cache=str()

for i in range(1,l+1):
    if A1[i]==True:
        s.append(cache)
        cache=str()
    if A1[i]==False:
        cache=cache+A[i]
              
A=np.array(A)
A1=np.array(A1)

GC=list()     
for i in s:
   GC_content=((np.sum(np.array(list(i))=="G")+np.sum(np.array(list(i))=="C"))/len(list(i)))*100
   GC.append(GC_content)


DF={"Names":list(A[A1[0:l]]),"GC content":GC}
DF=pd.DataFrame(DF)
M=M=max(DF[DF.columns[1]])
Test=np.where(DF[DF.columns[1]]==M)

print(DF)
print(DF[DF.columns[0]][int(Test[0])], "\n", M, sep="")
