in_string="""AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"""

import pandas as pd
import numpy as np

#Step1
sequence=["UUU", "UUC","UUA", "UUG","CUU", "CUC", "CUA", "CUG","AUU", "AUC", "AUA", "AUG",
          "GUU", "GUC", "GUA", "GUG","UCU", "UCC", "UCA", "UCG","CCU", "CCC", "CCA", "CCG",
          "ACU", "ACC", "ACA", "ACG",
          "GCU", "GCC", "GCA", "GCG",
          "UAU", "UAC", "UAA", "UAG","CAU", "CAC", "CAA", "CAG", "AAU", "AAC", "AAA", "AAG",
          "GAU", "GAC", "GAA", "GAG", "UGU", "UGC", "UGA", "UGG", "CGU", "CGC", "CGA", "CGG",
          "AGU", "AGC", "AGA", "AGG", "GGU", "GGC", "GGA", "GGG"]

amino_acid=["Phe","Phe", "Leu", "Leu", "Leu", "Leu", "Leu", "Leu","Ile", "Ile", "Ile", "Met",
            "Val", "Val", "Val", "Val","Ser", "Ser", "Ser", "Ser","Pro", "Pro", "Pro", "Pro",
            "Thr", "Thr", "Thr", "Thr","Ala", "Ala", "Ala", "Ala",
            "Tyr", "Tyr", "Stop", "Stop","His", "His", "Gln", "Gln", "Asn", "Asn", "Lys", "Lys",
            "Asp", "Asp", "Glu", "Glu", "Cys", "Cys", "Stop", "Trp","Arg", "Arg", "Arg", "Arg",
            "Ser", "Ser", "Arg", "Arg", "Gly", "Gly", "Gly", "Gly"]


dict={"Sequence":sequence, "amino_acid":amino_acid}
df=pd.DataFrame(dict)


a=0
b=3
All=list()
for i in range(1,len(in_string)):
    A=in_string[a:b]
    a+=3
    b+=3
    Bool=df["Sequence"]==A
    Return=df.amino_acid[Bool].to_numpy()[0]
    All.append(Return)
    
    if b>=(len(in_string)+1):
        break
    


#Step2
amino1=["Ala", "Arg", "Asn", "Asp", "Cys", "Glu","Gln",
        "Gly", "His", "Ile", "Leu", "Lys", "Met", "Phe", "Pro", "Ser", "Thr", "Trp", "Tyr", "Val", "Stop"]
amino2=["A","R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W","Y", "V", "Stop"]

df2={"Amino1":amino1, "Amino2":amino2}
df2=pd.DataFrame(df2)


All2=list()
for i in range(0,len(All)):
    Bool=df2["Amino1"]==All[i]
    Return=df2.Amino2[Bool].to_numpy()[0]
    if Return =="Stop":
        break
    else:
        All2.append(Return)
        
print("".join(All2))

    
##This can probably be done in one step
##it would be faster, however now you have dictionaries that enable 
##you to convert RNA string to 2 types of annotation
