def hamming_dist(dna1,dna2):
    diff=0
    for i in range(len(dna1)):
        if dna1[i]!=dna2[i]:
            diff+=1
    return diff
hamming_dist('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT')
