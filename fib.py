"""
Fibonacci sequence
Given: Positive integers n <= 40 and k <=5
Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in 
each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs"""

def fibonacci(n, k):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1, k) + k * fibonacci(n - 2, k)

if __name__ == "__main__":
    with open(r"C:/Users/admin/Downloads/rosalind_fib.txt", 'r') as f:
        n, k = f.readline().strip().split(" ")
        print(fibonacci(int(n), int(k)))
              