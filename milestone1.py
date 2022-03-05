#s(dna)
def s(dna):
    d = dict()
    for i in dna:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    return(d)

#dna2rna(dna)
def dna2rna(dna):
    rna = ""
    for char in dna:
        if char == "T":
            rna += "U"
        else:
            rna += char
    return rna

#reverse_complement(dna)
def reverse_complement(dna):
    dna = dna[::-1]
    revcomdna = ""
    complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
    for char in (dna):
        revcomdna += complements[char]
    return revcomdna

#mendels_law(hom,het,rec)
def mendels_law(hom,het,rec):
    total = hom + het + rec
    x = (hom*(hom-1)+2*hom*het+2*hom*rec+het*rec)
    y = 3*het*(het-1)
    z = 4*total*(total-1)
    
    return (4*x+y)/z

#fibonacci_rabbits(n,k)
def fibonacci_rabbits(n, k):
    if (n == 0 or n == 1 or n == 2):
        return 1
    return fibonacci_rabbits(n-1, k) + (fibonacci_rabbits(n-2, k)*k)

#gc_content(dna_list)
def gc_content(dna_list):
    maxProb = 0
    k = -1
    for i in dna_list:
        count = 0;
        for j in i:
            if (j == 'G' or j == 'C'):
                count += 1
        prob = count / len(i)
        indexs = dna_list.index(i)
        
        if (prob > maxProb and indexs > k):
            k = indexs
            maxProb = prob
            
    return (k,maxProb*100)

#Hamming_disk
def hamming_dist(dna1,dna2):
    diff=0
    for i in range(len(dna1)):
        if dna1[i]!=dna2[i]:
            diff+=1
    return diff

#Locate_substring
def locate_substring(dna_snippet, dna):
    start = 0
    li=[]
    while True: 
        if dna.find(dna_snippet, start)==-1:
            break
        else:
            start=dna.find(dna_snippet, start)
            li.append(start)
            start += 1 
    return li

#Rna2codon(rna)
def rna2codon(rna):
    genetic_code = {"UUU" : "F", "CUU": "L", "AUU": "I", "GUU": "V",
          "UUC" : "F", "CUC": "L", "AUC": "I", "GUC": "V",
          "UUA" : "L", "CUA": "L", "AUA": "I", "GUA": "V",
          "UUG" : "L", "CUG": "L", "AUG": "M", "GUG": "V",
          "UCU" : "S", "CCU": "P", "ACU": "T", "GCU": "A",
          "UCC" : "S", "CCC": "P", "ACC": "T", "GCC": "A",
          "UCA" : "S", "CCA": "P", "ACA": "T", "GCA": "A",
          "UCG" : "S", "CCG": "P", "ACG": "T", "GCG": "A",
          "UAU" : "Y", "CAU": "H", "AAU": "N", "GAU": "D",
          "UAC" : "Y", "CAC": "H", "AAC": "N", "GAC": "D",
       "UAA" : "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
       "UAG" : "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
          "UGU" : "C", "CGU": "R", "AGU": "S", "GGU": "G",
          "UGC" : "C", "CGC": "R", "AGC": "S", "GGC": "G",
       "UGA" : "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
          "UGG" : "W", "CGG": "R", "AGG": "R", "GGG": "G"}
    result = ""
    for i in range(0,len(rna),3):
        triplet = str(rna[i] + rna[i+1] + rna[i+2])
        if triplet in genetic_code:
            if genetic_code[triplet]=='Stop':
                break
        result = result + genetic_code[triplet]
    return result

#MUSKAN10

def count_dom_phenotype(genotypes):
    output = 0
    for n in range(0 ,6):
    	if n <= 2:
            output += genotypes[n] * 2
    	elif n == 3:
            output += genotypes[n] * 1.5
    	elif n == 4:
            output += genotypes[n]
    	else :
            continue
    return output





#MUSKAN11

def source_rna(protein):
    count = 1
    dict = {'F' : 2, 'L' : 6, 'S' : 6, 'Y' : 2, 'C' : 2, 'W' : 1, 'P' : 4, 'H' : 2, 'Q' : 2, 'R' : 6, 'I' : 3, 'M' : 1, 'T' : 4,
        	'N' : 2, 'K' : 2, 'V' : 4, 'A' : 4, 'D' : 2, 'E'  :2, 'G' : 4}
    for a in protein:
        count = count * dict[a]*3
    return count%1000000
#print result for sequence "MA"


#12
def splice_rna(dna, intron_list):
    proteinString = ''
    for i in intron_list:
        dna = dna.replace(i, '')
    rna = dna2rna(dna)
    proteinString = rna2codon(rna)
    return proteinString



