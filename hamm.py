"""
the Hamming distance
Given two strings s and t of equal length, the Hamington distance between s and t is the number of corresponding 
symbols that differ in s and t"""

def hamming(string_s, string_t):
    distance = 0
    assert len(string_s) == len(string_t)
    for i, j in zip(string_s, string_t):
        if i != j:
            distance += 1
    return distance


if __name__ == "__main__":
    with open(r"C:/Users/admin/Downloads/rosalind_hamm.txt", 'r') as f:
        string_s = f.readline().strip()
        string_t = f.readline().strip()
    print(hamming(string_s, string_t))