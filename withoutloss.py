import pandas as pd
import math
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans, vq
labeled_dataset_new=pd.read_csv('C:/Users/chaithu/Desktop/Bilgiprocess/extract.csv')
set1=list(labeled_dataset_new['Labeled'])
set2=list(set(set1))
set3=labeled_dataset_new[labeled_dataset_new['Labeled']==set2[0]]
set4=labeled_dataset_new[labeled_dataset_new['Labeled']==set2[1]]
l1=len(set3)
l2=len(set4)
distortionlist=[]
def to_number(s):
    try:
        s1 = float(s)
        return s1
    except ValueError:
        return s
converted = set3.apply(lambda f : to_number(f[0]) , axis = 1) 
for i in range(1,int(l1/l2)):
    codebook, distortion = kmeans(converted, i)
    distortionlist.append(distortion)
hon=[]
koku=int(l1/l2)
piu=list(range(1,koku))
def slope(x1,y1,x2,y2):
    return (y1 - y2) / (x1 - x2)
for i in range(len(distortionlist)-1):
    hon.append(slope(piu[i],distortionlist[i],piu[i+1],distortionlist[i+1]))
for i in range(len(hon)):
    if hon[i]<0:
        hon[i] = -hon[i]    
pun=hon.index(max(hon))
k=piu[pun+1]
codebook, distortion = kmeans(converted, k)
code, dist = vq(converted, codebook)
distances=list(dist)
code1=list(code)
u=pd.DataFrame(distances)
v=pd.DataFrame(code1)
t=set3.assign(distances=u.values)
s=t.assign(clusternumber=v.values)
puki=list(set(code1))
keku=[]
for i in range(len(puki)):
    keku.append(s[s['clusternumber']==puki[i]])
p=[]
for i in range(len(keku)):
    print("cluster",i,"length",len(keku[i]))
pap=int(input("enter the number of nearest elements per clusters"))
for j in range(pap):
    for i in range(len(keku)):
        p.append(keku[i].loc[[keku[i]['distances'].idxmin()]])
        keku[i]=keku[i].drop(keku[i]['distances'].idxmin())
training_set=pd.concat(p)
del training_set['distances']
del training_set['clusternumber']
training_set1=training_set.assign(Labeled=set2[0])
training_set_result=pd.concat([training_set1,set4])
