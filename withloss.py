import pandas as pd
labeled_dataset_new=pd.read_csv('C:/Users/chaithu/Desktop/Bilgiprocess/extract.csv')
set1=list(labeled_dataset_new['Labeled'])
set2=list(set(set1))
set3=labeled_dataset_new[labeled_dataset_new['Labeled']==set2[0]]
set4=labeled_dataset_new[labeled_dataset_new['Labeled']==set2[1]]
l1=len(set3)
l2=len(set4)
k=int(l1/l2)
del set3['Labeled']
from scipy.cluster.vq import kmeans, vq
 def to_number(s):
    try:
        s1 = float(s)
        return s1
    except ValueError:
        return s
converted = set3(lambda f : to_number(f[0]) , axis = 1) 
codebook, distortion = kmeans(converted, k)
code, dist = vq(converted, codebook)
code1=list(code)
d = {x:code1.count(x) for x in code1}
a, b = d.keys(), d.values()
f=l2
list1=range(len(code))
list2=range(len(codebook))
list3=list(code)
list4=list(codebook)
dist=zip(list1,list3)
dist1=zip(list2,list4)
val=dict(dist)
val2=dict(dist1)
ab=list(a)
bc=list(b)
clusless=[]
for i in range(len(d)):
    if(bc[i]<f):
        clusless.append(ab[i])
total=list(range(len(d)))
clusmore=list(set(total)-set(clusless))
inde=[]
sinde=[]
for i in range(len(clusless)):
    inde=[]
    for j in range(len(clusmore)):
        dist=abs(codebook[clusless[i]]-codebook[clusmore[j]])
        inde.append(dist)
    po=inde.index(min(inde))
    sinde.append(po)
coding=list(code)
for i in range(len(coding)):
    for j in range(len(sinde)):
        if(coding[i]==clusless[j]):
               coding[i]=clusmore[sinde[j]]
labul=pd.DataFrame(coding)
set3=set3.assign(labul=labul.values)
tu=list(set(coding))
listing=[]
for i in range(len(tu)):
    listing.append(set3[(set3['labul']==tu[i])])
for i in range(len(listing)):
      listing[i]['labul']=0

resulttrainingset=[]
for i in range(len(listing)):
    frames = [listing[i],set4]
    resulttrainingset.append(pd.concat(frames,ignore_index=True))
