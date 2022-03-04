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
print(locate_substring("ATAT","GATATATGCATATACTT"))
