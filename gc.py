"""
Calculation of GC-content
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each)
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
"""

from Bio import SeqIO

def cal_gc(strings):
    gc_contents = {}
    for k, v in strings.items():
        gc_content = (v.count("C") + v.count("G")) / len(v)
        gc_contents[k] = gc_content

    gc_contents = sorted(gc_contents.items() , key = lambda d: d[1], reverse = True)
    highest_gc = gc_contents[0]
    return highest_gc

if __name__ == "__main__":
    # load data
    seq_name, seq_string = [], []
    with open(r"C:/Users/admin/Downloads/rosalind_gc (1).txt", 'r') as f:
        for seq_record in SeqIO.parse(f, 'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))
    
    strings = {seq_name[i]: seq_string[i] for i in range(len(seq_name))}
    highest_gc = cal_gc(strings)
    print(highest_gc[0])
    print(highest_gc[1] * 100)

