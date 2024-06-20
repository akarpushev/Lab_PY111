import pprint


def knapsack(values, weights, W):
    n = len(values)
    dp = [[0] * (W * 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp



if __name__ == '__main__':
    values = [120, 100, 150]
    weights = [1, 2, 3]
    W = 5
    pprint.pprint(knapsack(values, weights, W))
    #print(knapsack(values, weights, W))

