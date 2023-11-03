inputFilePath = "C:/Users/admin/Downloads/rosalind_splc.txt"
outputFilePath = "C:/Users/admin/Downloads/rosalind_splc_answer.txt"

from itertools import permutations
import re

def fastaRead(filename):
    """This reads the Rosalind file and turns the sequences into a list, changes the keys to numbers"""
    fasta = {}
    rosalindFile = "false"
    oneString = ""
    with open(filename, "r") as file_test:
        for tmpline in file_test:
            tmpline = tmpline.strip()
            if tmpline.startswith(">"):
                rosalindFile = "true"
            elif (rosalindFile == "false"):
                oneString += tmpline
    if(rosalindFile == "false"):
        return oneString
    count = -1
    with open(filename, "r") as file_one:
        for line in file_one:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                count += 1
                fasta[count] = []
                continue
            sequence = line
            fasta[count].append(sequence)
        numberDictKey = len(fasta)
        numberOfValueInKey = 0
        singleDna = ""
        for numberDictKey in fasta:
            valuesInKey = fasta[numberDictKey]
            numberOfValueInKey = len(valuesInKey)

            for numberOfValueInKey in valuesInKey:
                singleDna += numberOfValueInKey

                fasta[numberDictKey] = singleDna
            singleDna = ""
    return fasta

print ("Get the strings into a dictionary...")
rosalindDict = fastaRead(inputFilePath)

#Set the index for traversing the dictionary
indexForExons = rosalindDict.__len__()

#Get the original string
originalString = rosalindDict[0]

print ("Removing codons...")
#Remove the condons
for i in range(1, indexForExons):
    originalString = re.sub(rosalindDict[i], '', originalString)

print ("Changing RNA to DNA...")
#Change the RNA to DNA
originalString = originalString.replace("T", "U")

print ("Change the RNA to Proteins...")
lenOfStr = len(originalString)
newStr = ""
a=0
b=3
i=0

str = originalString[a:b]

while i<lenOfStr :
	if "UUU" in str:
		newStr += 'F'
	if "UUC" in str:
		newStr += 'F'
	if "UUA" in str:
		newStr += 'L'
	if "UUG" in str:
		newStr += 'L'

	if "UCU" in str:
		newStr += 'S'
	if "UCC" in str:
		newStr += 'S'
	if "UCA" in str:
		newStr += 'S'
	if "UCG" in str:
		newStr += 'S'

	if "UAU" in str:
		newStr += 'Y'
	if "UAC" in str:
		newStr += 'Y'
	if "UAA" in str:
		break
	if "UAG" in str:
		break

	if "UGU" in str:
		newStr += 'C'
	if "UGC" in str:
		newStr += 'C'
	if "UGA" in str:
		break
	if "UGG" in str:
		newStr += 'W'

	if "CUU" in str:
		newStr += 'L'
	if "CUC" in str:
		newStr += 'L'
	if "CUA" in str:
		newStr += 'L'
	if "CUG" in str:
		newStr += 'L'

	if "CCU" in str:
		newStr += 'P'
	if "CCC" in str:
		newStr += 'P'
	if "CCA" in str:
		newStr += 'P'
	if "CCG" in str:
		newStr += 'P'

	if "CAU" in str:
		newStr += 'H'
	if "CAC" in str:
		newStr += 'H'
	if "CAA" in str:
		newStr += 'Q'
	if "CAG" in str:
		newStr += 'Q'

	if "CGU" in str:
		newStr += 'R'
	if "CGC" in str:
		newStr += 'R'
	if "CGA" in str:
		newStr += 'R'
	if "CGG" in str:
		newStr += 'R'

	if "AUU" in str:
		newStr += 'I'
	if "AUC" in str:
		newStr += 'I'
	if "AUA" in str:
		newStr += 'I'
	if "AUG" in str:
		newStr += 'M'

	if "ACU" in str:
		newStr += 'T'
	if "ACC" in str:
		newStr += 'T'
	if "ACA" in str:
		newStr += 'T'
	if "ACG" in str:
		newStr += 'T'

	if "AAU" in str:
		newStr += 'N'
	if "AAC" in str:
		newStr += 'N'
	if "AAA" in str:
		newStr += 'K'
	if "AAG" in str:
		newStr += 'K'

	if "AGU" in str:
		newStr += 'S'
	if "AGC" in str:
		newStr += 'S'
	if "AGA" in str:
		newStr += 'R'
	if "AGG" in str:
		newStr += 'R'

	if "GUU" in str:
		newStr += 'V'
	if "GUC" in str:
		newStr += 'V'
	if "GUA" in str:
		newStr += 'V'
	if "GUG" in str:
		newStr += 'V'

	if "GCU" in str:
		newStr += 'A'
	if "GCC" in str:
		newStr += 'A'
	if "GCA" in str:
		newStr += 'A'
	if "GCG" in str:
		newStr += 'A'

	if "GAU" in str:
		newStr += 'D'
	if "GAC" in str:
		newStr += 'D'
	if "GAA" in str:
		newStr += 'E'
	if "GAG" in str:
		newStr += 'E'

	if "GGU" in str:
		newStr += 'G'
	if "GGC" in str:
		newStr += 'G'
	if "GGA" in str:
		newStr += 'G'
	if "GGG" in str:
		newStr += 'G'

	a += 3
	b += 3
	str = originalString[a:b]

	i += 1

#Write everything to the output file path
with open(outputFilePath, 'w') as f:
    f.write(newStr)
    print ("Permutations have been written to: " + outputFilePath)