"""
Transribing DNA into RNA
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

def replace(string):
    replaced_string = string.replace("T", "U")
    return replaced_string

if __name__ == "__main__":
    with open(r"C:\Users\admin\Downloads\rosalind_rna.txt", 'r') as f:
        string = f.readline().strip()
        replaced_string = replace(string)
        print(replaced_string)