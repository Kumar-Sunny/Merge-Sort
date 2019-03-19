import time
import sys
import random
sys.setrecursionlimit(10000000)

def MergeSort(a,s,e):
    if(s<e):
        m=(s+e)//2
        MergeSort(a,s,m)
        MergeSort(a,m+1,e)
        A=Merge(a,s,m,e)
        return A


def Merge(a,s,m,e):
    n1=m-s+1
    n2=e-m
    L=[]
    R=[]
    for i in range(n1):
        L.append(a[s+i])
    for j in range(n2):
        R.append(a[m+j+1])
    L.append(1000)
    R.append(1000)
    i=j=0
    for k in range(s,e+1):
        if L[i]<=R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
    return a

n=int(input("Enter the number of test Cases:"))

bCase=[]
wCase=[]
avgCase=[]
for i in range(n):
    s=int(input())
    arr=[]
    for j in range(s):
        arr.append(random.randrange(100))
    #AverageCase
    st=time.time()
    MergeSort(arr,0,s-1)
    ed=time.time()
    avgCase.append(ed-st)
    #BestCase
    st=time.time()
    MergeSort(arr,0,s-1)
    ed=time.time()
    bCase.append(ed-st)
    #WorstCase
    arr.reverse()
    st=time.time()
    MergeSort(arr,0,s-1)
    ed=time.time()
    wCase.append(ed-st)
print("\n\nBest Case: ",bCase)
print("\n\nAverage Case: ",avgCase)
print("\n\nWorst Case: ",wCase)