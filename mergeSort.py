import matplotlib.pyplot as plt
import numpy as np
def merge(arr,l,m,r):
  n1=m-l+1
  n2=r-m
  L=[0]*n1
  R=[0]*n2
  for i in range(n1):
    L[i]=arr[l+i]
  for j in range(n2):
    R[j]=arr[m+1+j]
  i=j=0
  k=l
  while i<n1 and j<n2:
    if(L[i]<R[j]):
      arr[k]=L[i]
      i+=1
    else:
      arr[k]=R[j]
      j+=1
    k+=1
  while i<n1:
    arr[k]=L[i]
    k+=1
    i+=1
  while j<n2:
    arr[k]=R[j]
    k+=1
    j+=1
def mergeSort(arr,l,r):
  if(l<r):
    m=(l+r)//2
    mergeSort(arr,l,m)
    mergeSort(arr,m+1,r)
    merge(arr,l,m,r)
print("Enter n:")
n=int(input())
print("Enter array:")
arr=list(map(int,input().strip().split()))[:n]
mergeSort(arr,0,len(arr)-1)
print("Sorted array:")
print(arr)
##Plotting graph
n=np.array([1,50,100,500,1000,1500,2000])
y=(n*np.log(n))
plt.figure(figsize=(8,5))
plt.plot(n,y)
plt.title("Complxity of o(nlogn)")
plt.show()
