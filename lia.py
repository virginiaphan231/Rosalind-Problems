"""
Independent Alleles
url: http://rosalind.info/problems/lia/

Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
"""

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f  = f *i
    return f

def combination(i, j):
    return factorial(i)/(factorial(j) * factorial(i - j))

def independent_alleles(k, n):
    p = 0
    count = pow(2, k)                        
    for i in range(n, count+1):
        p += combination(count, i) * pow(0.25, i) * pow(0.75, count - i)
    return p

if __name__ == "__main__":
    with open("C:/Users/admin/Downloads/rosalind_lia.txt", "r") as f:
        k, n = [int(i) for i in f.readline().strip().split(" ")]
    print(independent_alleles(k,n))