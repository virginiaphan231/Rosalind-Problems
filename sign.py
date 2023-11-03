"""
Enumerating Oriented Gene Orderings

Given: A positive integer n≤6.
Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
"""

import itertools

def SignedPermutation(n):
    list1 = []
    for i in range(n):
        list1.extend([i + 1, - i - 1])
    list2 = list(itertools.permutations(list1, n))

    list3 = []
    for a in list2:
        aset = set()
        for i in a:
            aset.add(abs(i))
        if len(aset) < len(a):
            list3.append(a)

    list4 = list(set(list2) ^ set(list3))
    with open("C:/Users/admin/Downloads/rosalind_sign_result.txt", "w") as f:
        f.write(str(len(list4)))
        f.write("\n")
        for i in list4:
            a = str(i)
            a = a.replace('(', '').replace(',', '').replace(')', '')
            f.write(a + "\n")

if __name__ == "__main__":
    with open("C:/Users/admin/Downloads/rosalind_sign.txt", "r") as f:
        n = int(f.readline().strip())
        SignedPermutation(n)
        print("Result saved")
    