def list_of_primes(n):
    if n <= 2:
        return 0
    dp = [True] * n
    dp[0] = dp[1] = False
    for i in range(2, n):
        if dp[i]:
            for j in range(i * i, n, i):
                dp[j] = False
    return [i for i, num in enumerate(dp) if num]


print(list_of_primes(20))
