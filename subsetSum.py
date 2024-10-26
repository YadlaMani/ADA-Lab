def subsetSum(arr,n,idx,res,k,temp):
    if(idx==n):
        if(k==0):
            res.append(temp[:])
        return
    subsetSum(arr,n,idx+1,res,k,temp)
    if(k>=arr[idx]):
        temp.append(arr[idx])
        subsetSum(arr,n,idx+1,res,k-arr[idx],temp)
        temp.pop()
    
    
n=int(input("Enter n:"))

arr=list(map(int,input().strip().split()))[:n]
k=int(input("Enter the sum:"))
res=[]
temp=[]
subsetSum(arr,n,0,res,k,temp)#array,size,index,result array,sum,temp array to push the taken element
print(f"The subsets having sum {k} are:\n{res}")