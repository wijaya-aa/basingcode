def knapsack_top_down(W, Wt, Val, n, memo = None):
    if memo is None:
        memo = {}
    if  (n, W) in memo:
        return memo[(n, W)]
    if n == 0 or W == 0:
        return 0
    if Wt [n - 1] > W:
        memo[(n,W)] = knapsack_top_down(W, Wt, Val,n - 1, memo)
        return memo[(n, W)]
    else:
        memo[(n, W)] = max(Val[n - 1] + knapsack_top_down(W - Wt [n -1], Wt, Val, n - 1, memo), knapsack_top_down(W, Wt, Val, n - 1, memo))
        return memo[(n, W)]
    
W = 50
Wt = [10, 20 ,30]
Val = [60, 100, 120]
n = len(Val)
print(knapsack_top_down(W, Wt, Val, n))