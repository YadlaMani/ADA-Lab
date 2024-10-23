class Job:
    def __init__(self,day,profit,id):
        self.day=day
        self.profit=profit
        self.id=id
def jobSequencing(jobs,days):
    jobs=sorted(jobs,key=lambda job:job.profit,reverse=True)
    TotalProfit=0
    res=['-1']*(days)
    for job in jobs:
        idx=job.day-1
        while(res[idx]!='-1' and idx>=0):
            idx-=1
        if(res[idx]=='-1'):
            res[idx]=job.id
            TotalProfit+=job.profit
    print("The job sequence:")
    print(res)
    return TotalProfit

n=int(input("Enter number of jobs:"))
jobs=[]
for i in range(n):
    profit=int(input(f"Enter profit[{i+1}]:"))
    day=int(input(f"Enter day[{i+1}]:"))
    id=input(f"Enter id[{i+1}]")
    jobs.append(Job(day,profit,id))
days=int(input("Enter the no.of days:"))
TotalProfit=jobSequencing(jobs,days)
print(f"Total profit {TotalProfit} ")


