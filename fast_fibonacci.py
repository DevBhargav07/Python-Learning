#!/usr/bin/env python3

"""
This is used to calculate fibonacci
"""

def fibonacci(n: int) -> int:
    """
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    """
    if n < 0:
        raise("Negative values are not supported")
    return _fib(n)[0]

def _fib(n: int) -> tuple[int, int]:
    if n == 0:
        return (0, 1)
    a, b = _fib(n // 2)
    c = a * (b * 2 - a)
    d = a * a + b * b
    return (d, c + d) if n % 2 else (c, d)

if __name__ == "__main__":
    n = int(input())
    print(f"fibonacci({n}): {fibonacci(n)}")
