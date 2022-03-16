#number of months
n=5
#number of offspring pairs
offspring_pairs=3
cache=list()
for i in range(1,n+1):
        if i ==1:
            Little_rabit_pairs=1
            mature_rabit_pairs=0
            a=Little_rabit_pairs+mature_rabit_pairs
            cache.append(a)
        if i ==2:
            Little_rabit_pairs=0
            mature_rabit_pairs=1
            m_ca=mature_rabit_pairs
            l_ca=Little_rabit_pairs
            a=Little_rabit_pairs+mature_rabit_pairs
            cache.append(a)
        if i>2:
            Little_rabit_pairs=m_ca*offspring_pairs
            mature_rabit_pairs=m_ca+l_ca
            m_ca=mature_rabit_pairs
            l_ca=Little_rabit_pairs
            a=Little_rabit_pairs+mature_rabit_pairs
            cache.append(a)
            
print(cache[-1])
