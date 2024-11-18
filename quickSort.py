def partition(arr,l,r):
  pivot=arr[r]
  i=l-1
  for j in range(l,r):
    if(arr[j]<=pivot):
      i+=1
      arr[i],arr[j]=arr[j],arr[i]
  arr[i+1],arr[r]=arr[r],arr[i+1]
  return i+1
def quickSort(arr,l,r):
  if(l<r):
    pi=partition(arr,l,r)
    quickSort(arr,l,pi-1)
    quickSort(arr,pi+1,r)
  return arr
n=int(input("Enter n:"))
arr=list(map(int,input("Enter the array elements:").strip().split()))[:n]
quickSort(arr,0,len(arr)-1)
print("Sorted array:")
print(arr)
#plotting graph
import numpy as np
import matplotlib.pyplot as plt
n=np.array([1,2,3,4,5])
y=np.array([1,4,9,16,25])
plt.plot(n,y)
plt.xlabel('n')
plt.ylabel('n^2')
plt.show()
