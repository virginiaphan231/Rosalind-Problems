"""
Ordering Strings of Varying Length Lexicographically

Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).
Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)
"""

import itertools

with open("C:/Users/admin/Downloads/rosalind_lexv.txt", "r") as f:
    symbols = f.readline().strip().replace(" ", "")
    n = int(f.readline().strip())
# print(symbols, n)

strings = []
for i in range(1,n+1):
    for j in list(itertools.product(symbols, repeat = i)):
        strings.append("".join(j))
# print(len(strings))

for s in strings:
    for i in range(len(s)-1):
        f=False
        for j in range(i+1, len(s)):
            if symbols.index(s[i]) > symbols.index(s[j]):
                strings.remove(s)
                f = True
                break
        if f:
            break
# print(len(strings))
#print("\n".join(strings))

with open("C:/Users/admin/Downloads/rosalind_lexv_output.txt", "w") as f:
    for s in strings:
        f.write(s + "\n")
print("Result saved")