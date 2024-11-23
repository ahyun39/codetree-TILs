from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def find_lcm_recursive(numbers, n):
    if n == 1:
        return numbers[0]
    return lcm(numbers[n-1], find_lcm_recursive(numbers, n-1))

def f():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(find_lcm_recursive(numbers, n))

if __name__ == "__main__":
    f()