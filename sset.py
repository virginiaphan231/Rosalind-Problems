"""
Counting Subsets
url: http://rosalind.info/problems/sset/

Given: A positive integer n (n≤1000).
Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.
"""

import math
from scipy.special import comb, perm

with open("C:/Users/admin/Downloads/rosalind_sset (1).txt", "r") as f:
    n = int(f.readline().strip())
print(2**n % 1000000)

