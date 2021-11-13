##...RISHUL GHOSH...##
##...N230...##

val = [24, 18, 18, 10]
wt = [24, 10, 10, 7]
W = 50
n = len(val)

t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + knapsack(
                wt, val, W-wt[n-1], n-1),
            knapsack(wt, val, W, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W, n-1)
        return t[n][W]

print("Profits = ",val)
print("Respective Weights = ",wt)
print("Max Knapsack Weight Capacity = ",W)
print("Answer = ",knapsack(wt, val, W, n))




