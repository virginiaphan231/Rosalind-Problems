""" 
Error Correction in Reads
url: http://rosalind.info/problems/corr/

Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read s in the dataset, one of the following applies: s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement); s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).
Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)
"""

inputFilePath = "C:/Users/admin/Downloads/rosalind_corr.txt"
outputFilePath = "C:/Users/admin/Downloads/rosalind_corr_answer.txt"

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

def reverse_comp(dnaStrand):
	"""This function gets the reverse complement of the strand"""
	complementDNA = ""

	dnaSequence = list(dnaStrand)
	dnaSequence.reverse()

	dnaStrand = ''.join(dnaSequence)
	complementDict = {"C": "G", "G": "C", "T": "A", "A": "T"}

	for base in dnaStrand:
		complementDNA += complementDict[base]

	return complementDNA

def hammingDistance(a,b):
    """This gets the hamming distance for two inputs"""
    hamming = 0
    for x, y in zip(a, b):
        if x != y:
            hamming += 1
    return hamming

#Get each read and fix single-nucleotide error
with open(outputFilePath, 'w') as f:
    answerList = []
    sequenceList = []

    correctSequencesList = []
    incorrectSequencesList = []
    sequenceKeys = fastaRead(inputFilePath)
    for i in sequenceKeys:
        sequenceList.append(sequenceKeys[i])

    #Count the number of times the sequence and reverse comp of that sequence are in the original list
    for sequence in sequenceList:
        numberOfDuplicates = sequenceList.count(sequence) + sequenceList.count(reverse_comp(sequence))
        if sequence == reverse_comp(sequence):
            numberOfDuplicates -= 1
        if numberOfDuplicates > 1:
            if sequence not in correctSequencesList:
                if reverse_comp(sequence) not in correctSequencesList:
                    correctSequencesList.append(sequence)
        else:
            incorrectSequencesList.append(sequence)

    for incorrectSequence in incorrectSequencesList:
        for correctSequence in correctSequencesList:
            if hammingDistance(incorrectSequence, correctSequence) == 1:
                answerList.append(incorrectSequence + "->" + correctSequence)
            elif hammingDistance(incorrectSequence, reverse_comp(correctSequence)) == 1:
                answerList.append(incorrectSequence + "->" + reverse_comp(correctSequence))

    for item in list(set(answerList)):
        f.write('{}'.format(item) + "\n")

print ("Corrections have been written to: " + outputFilePath)