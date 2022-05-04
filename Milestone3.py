import copy
import random

def load_file(fname):
    try:
        with open(fname, 'r', encoding='utf-8') as filename:
            data = fielname.read().splitlines()
            return data

    except OSError:
        print("File not found")


def assemble_genome2(data):

    lengthTotal = len(data)
    idx = random.randint(0, lengthTotal - 1)

    find_dna = data.pop(idx)
    lengthTotal = lengthTotal - 1

    while lengthTotal > 0:
        print(lengthTotal)
        isValid = True
        for i in range(8, 0, -1): 
            for j in range(lengthTotal):
                if find_dna[0 : i] == data[j][-i:]:
                    find_dna = data.pop(j) + find_dna[i:]
                    lengthTotal = lengthTotal - 1
                    isValid = False
                    break

                elif find_dna[-i:] == data[j][0:i]:
                    find_dna = find_dna + data.pop(j)[i:]
                    lengthTotal = lengthTotal - 1
                    isValid = False
                    break
            if not isValid:
                break

        if isValid:
            print("*********************")
            print(find_dna)
            data1 = data.pop()
            print(data1)
            find_dna = find_dna + data1
            lengthTotal = lengthTotal - 1
            
    print("Finished. Final length is:", lengthTotal, data)
    return find_dna

M3.py
M3.py 표시 중입니다.
