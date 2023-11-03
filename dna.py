"""
Given a DNA string s of length as most 1000 nt
Return: Four integers counting the respective number of times that the symbols 'A', 'C', 'G', 'T' occur in s"""


def count_nucleotides(string):
    num_A = string.count("A")
    num_C = string.count("C")
    num_G = string.count("G")
    num_T = string.count("T")
    return num_A, num_C, num_G, num_T

if __name__ == "__main__":
    with open(r"C:\Users\admin\Downloads\rosalind_dna.txt", 'r') as f:
        string = f.readline().strip()
        num_A, num_C, num_G, num_T = count_nucleotides(string)
        print(num_A, num_C, num_G, num_T)