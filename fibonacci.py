#fibonacci series using dp
def fibonacci(n):
    """
    Using recursion method here
    """
    if n <= 1:
        return n
    return fibonacci(n- 1) + fibonacci(n - 2)

def fibonacci_dp(n, dp):
    """
    Using recursion with memorization
    """
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibonacci_dp(n - 1, dp) + fibonacci_dp(n-2, dp)
    return dp[n]

if __name__ == "__main__":
    n = int(input("Enter your prefered number of fibonacci series: "))
    print()
    print(fibonacci(n))
    dp = [-1] * (n + 1)
    print(fibonacci_dp(n, dp))
    # using tabulation method
    previous = 0
    current = 1
    i = 1
    while i != n:
        total = previous + current
        previous = current
        current = total
        i += 1
    print(current)


