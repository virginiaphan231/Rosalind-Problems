"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

def reversed_string(string):
    output = ""
    for i in string[:: -1]:
        if i == "A":
            output += "T"
        if i == "T":
            output += "A"
        if i == "C":
            output += "G"
        if i == "G":
            output += "C"
    return output

    
if __name__ == "__main__":
    with open(r"C:\Users\admin\Downloads\rosalind_revc (1).txt", 'r') as f:
        string = f.readline().strip()
        output = reversed_string(string)
        print(output)