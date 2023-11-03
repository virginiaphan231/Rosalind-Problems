"""
Finding a Shared Spliced Motif
url: http://rosalind.info/problems/lcsq/

Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.
Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)
"""

import yaml
from importlib import resources
from functools import cache


def resource_file(file):
    return resources.files("rosalind.resources").joinpath(file)


def yaml_resource(file):
    with open(resource_file(file)) as stream:
        return yaml.safe_load(stream)


def matrix_resource(file):
    lines = open(resource_file(file)).read().splitlines()
    header = lines[0].split()
    return {x[0]: dict(zip(header, map(int, x.split()[1:]))) for x in lines[1:]}


@cache
def genetic_code():
    return yaml_resource("genetic_code.yaml")


@cache
def codons():
    return yaml_resource("codons.yaml")


@cache
def aa_mass():
    return yaml_resource("aa_mass.yaml")


@cache
def blosum62():
    return matrix_resource("blosum62.txt")


@cache
def pam250():
    return matrix_resource("pam250.txt")

def lcsq(s1, s2):
    """Finding a Shared Spliced Motif"""
    # initialise
    m, p = {}, {}
    for j in range(len(s2) + 1):
        m[j, 0] = 0
        p[j, 0] = [j - 1, 0]

    for i in range(len(s1) + 1):
        m[0, i] = 0
        p[0, i] = [0, i - 1]

    # fill matrices
    for j in range(len(s2)):
        for i in range(len(s1)):
            if s1[i] == s2[j]:
                m[j + 1, i + 1] = m[j, i] + 1
                p[j + 1, i + 1] = [j, i]
            else:
                opt = [m[j + 1, i], m[j, i + 1]]
                m[j + 1, i + 1] = max(opt)
                p[j + 1, i + 1] = [[j + 1, i], [j, i + 1]][opt.index(max(opt))]

    # traceback
    subs = ""
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if p[j, i] == [j - 1, i - 1]:
            subs += s1[i - 1]
        j, i = p[j, i]

    return subs[::-1]


def main(file):
    print(lcsq(Parser(file).seqs()))

file = "C:/Users/admin/Downloads/rosalind_lcsq.txt"
main(file = file)