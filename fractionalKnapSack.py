class Item:
    def __init__(self,val,wt):
        self.val=val
        self.wt=wt
        self.ratio=val/wt
def fractionalKnapSack(cap,items):
    items=sorted(items,key=lambda item:item.ratio,reverse=True)
    Profit=0
    for item in items:
        if(cap==0):
            break
        stake=min(cap,item.wt)
        Profit+=(stake*item.ratio)
        cap-=stake
    return Profit
n=int(input("Enter n:"))
items=[]
for i in range(n):
    val=float(input(f"Enter value[{i+1}]:"))
    wt=float(input(f"Enter weight[{i+1}]:"))
    items.append(Item(val,wt))
cap=float(input("Enter the capacity of the sack:"))
Profit=fractionalKnapSack(cap,items)
print(f"Maximum profile of the knapsack is:{Profit}")