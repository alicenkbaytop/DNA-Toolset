from DNAToolkit import *

if __name__ == "__main__":
    rnDNAStr = "ataGCCa"
    #print(validateSeq(rnDNAStr))
    #print(randomDNASeq(10))
    seq = randomDNASeq(10)
    print(countNucType(seq))