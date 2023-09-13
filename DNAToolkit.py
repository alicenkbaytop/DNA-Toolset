import random
import collections

Nucleotides = ["A", "C", "G", "T"]

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()

    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def randomDNASeq(size:int):
    rnSeq = []

    for num in range(size):
        rnSeq.append(random.choice(Nucleotides))
        #rnSeq = "".join(random.choice(Nucleotides))
    
    return rnSeq

def countNucType(seq):
    NucDict = {"A":0, "C":0, "G":0, "T":0}

    for nuc in seq:
        if nuc == "A":
            NucDict["A"] +=1

        if nuc == "C":
            NucDict["C"] +=1

        if nuc == "G":
            NucDict["G"] +=1

        if nuc == "T":
            NucDict["T"] +=1

    return NucDict
    #return dict(collections.Counter(seq))

