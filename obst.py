def Sum(freq, i, j):
    return sum(freq[i:j + 1])
def printOBST(root, keys, i, j, level, is_left):
    if i > j:
        return

    r = root[i][j]
    indent = "   " * level
    direction = "Root" if level == 0 else ("L" if is_left else "R")
    print(f"{indent}{direction}: {keys[r]}")

   
    printOBST(root, keys, i, r - 1, level + 1, True)
    printOBST(root, keys, r + 1, j, level + 1, False)
def obst(keys,freq,n):
    cost=[[0 for _ in range(n)] for _ in range(n)]
    root=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        cost[i][i]=freq[i]
        root[i][i]=i
    for L in range(2,n+1):
        for i in range(n-L+1):
            j=i+L-1
            cost[i][j] = float('inf')
            for r in range(i, j + 1):
                left_cost = cost[i][r - 1] if r > i else 0
                right_cost = cost[r + 1][j] if r < j else 0
                total_cost = left_cost + right_cost + Sum(freq, i, j)
                if total_cost < cost[i][j]:
                    cost[i][j] = total_cost
                    root[i][j] = r
    print("Cost of Optimal BST is", cost[0][n - 1])
    print("\nThe structure of the Optimal BST is:")
    printOBST(root, keys, 0, n - 1, 0, True)
n=int(input("Enter no.of nodes:"))
keys=list(map(int,input("Enter keys:").strip().split()))[:n]
freq=list(map(int,input("Enter freqs:").strip().split()))[:n]
obst(keys,freq,n)