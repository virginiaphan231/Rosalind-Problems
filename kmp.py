"""
Speeding Up Motif Finding
url: http://rosalind.info/problems/kmp/

Given: A DNA string s (of length at most 100 kbp) in FASTA format.
Return: The failure array of s.
"""

from Bio import SeqIO

def _get_failure_array(s):
    failure_array = [0] * len(s)
    longest_motif_length = 0 
    for i in range(1, len(s)):
        print(i)
        for j in range(1, len(s)-i+1):
            if s[:i] == s[j:j+i]:
                failure_array[j+i-1] = len(s[:i])
                longest_motif_length = len(s[:i])
            # print(i, j)

        if longest_motif_length < len(s[:i]):
            break
    #print(failure_array)

if __name__ == "__main__":
#     # test
    # s = "CAGCATGGTATCACAGCAGAG"
    # failure_array = [0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 4, 5, 3, 0, 0]
    # _get_failure_array(s)

    with open ("C:/Users/admin/Downloads/rosalind_kmp.txt",'r') as fa:
        for seq_record in SeqIO.parse(fa,'fasta'):
            s = seq_record.seq    
    _get_failure_array(s)
    print("done!")