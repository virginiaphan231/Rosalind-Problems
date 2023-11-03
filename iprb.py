"""
MENDEL'S FIRST LAW
Given: Three positive integers k, m, n representing a population containing k + m + n organisms; 
k individuals are homozygous diminant for a factor, m are heterozygous and n are homozygous recessive
Return: The probability that two random selected mating organism will produce an individual possissing a dominant allele. """


def prob(k, m, n):
    i = m * m + 4 * n * n + 4 * m * n - 4 * n - m
    j = 4 * (k + m + n) * (k + m + n - 1)
    rst = 1 - float(i) / j
    return rst

if __name__ == "__main__":
    with open(r"C:/Users/admin/Downloads/rosalind_iprb (1).txt", 'r') as f:
        k, m, n = f.readline().strip().split(" ")
        print(prob(int(k), int(m), int(n)))