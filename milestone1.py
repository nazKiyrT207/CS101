#Upo 1
def s(dna):
    d = dict()
    for i in dna:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
     print(d)
