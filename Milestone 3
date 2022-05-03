import copy
import random

def load_file(fname):
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            data = f.read().splitlines()
            return data

    except OSError:
        print("File not found")


def assemble_genome2(data):
    # assume an eight-character overlap between strings
    total_len = len(data)
    index = random.randint(0, total_len-1)
    superDNA = data.pop(index)
    total_len -= 1
    while total_len > 0:
        print(total_len)
        BOOL = True
        for l in range(8, 0, -1): # 8,7,6,5,4,3,2,1 tot8 why 8-1? eight-character overlap between strings
            for i in range(total_len):
                if superDNA[0:l] == data[i][-l:]:
                    superDNA = data.pop(i) + superDNA[l:]
                    #print(superDNA)
                    total_len -= 1
                    BOOL = False
                    break
                elif superDNA[-l:] == data[i][0:l]:
                    superDNA = superDNA + data.pop(i)[l:]
                    #print(superDNA)
                    total_len -= 1
                    BOOL = False
                    break
            if not BOOL:
                break
        if BOOL:
            print("*********************")
            print(superDNA)
            d = data.pop()
            print(d)
            superDNA += d
            total_len -= 1
    print("Finish, with len:", total_len, data)
    return superDNA



#df = load_file("test5000.txt")
#res = assemble_genome2_v3(df)
#print(res)
