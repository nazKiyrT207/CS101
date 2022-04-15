def find_splice(dna_motif, dna):
  start = 0
  li = []
  for i in dna_motif:
    try:
      dna.index(i, start)
    except ValueError:
      return []
    li.append(dna.index(i, start))
    start = dna.index(i, start)+1
  return li
print(find_splice('GTA', "ACGACATCACGTGACG"))

def shared_motif(dna_list):
  firstDna = dna_list[0]
  l = len(firstDna)
  lcs = ""
  for i in range(l):
    for j in range(i,l):
      substring = firstDna[i:j+1]
      flag = True
      for k in dna_list:
        if substring not in k:
          flag = False
          break
      if flag:
        if len(substring) > len(lcs):
          lcs = substring
  return lcs
print(shared_motif(["GATTACA", "TAGACCA", "ATACA"]))
print(shared_motif(["ATATACA", "ATACAGA", "GGTATACA"]))

def perfect_match(rna):
	d = {}
	for i in rna:
		if i in d.keys():
			d[i] += 1
		else:
			d[i] = 1

	cg = 1
	au = 1

	for i in range(1, d['G']+1):
		cg *= i
	
	for i in range(1, d['U']+1):
		au *= i
	
	
	if d['C'] != d['G'] or d['A'] != d['U']:
		return 0
	else:
		return cg * au
import math

def random_genome(dna, gc):
	cg, at = 0, 0
	for i in dna:
		if i == 'A' or i == 'T':
			at += 1
		elif i == 'C' or i == 'G':
			cg += 1
	result = []
	for i in range(len(gc)):
		cg_val = cg * math.log10(float(gc[i]/2))
		at_val = at * math.log10((1-float(gc[i]))/2)
		result.append(round((cg_val+at_val), 3))
	return result 

dna = "ACGATACAA"
gc_content = [0.129, 0.287, 0.423, 0.476, 0.641, 0.742, 0.783]


print(random_genome(dna, gc_content))

def assemble_genome(words):
    def recursive_find(i, select):
        if select == 2**n - 1:
            return words[i]
        ans = "".join(words)
        for j in range(n):
            if select & 2**j == 0:
                conn = congruency[i][j]
                curr_word = recursive_find(j, (select | 2**j))
                if len(words[i] + curr_word[conn:]) < len(ans):
                    ans = words[i] + curr_word[conn:]
        return ans
    n = len(words)
    congruency = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                size = len(words[i])
                for k in range(1, size):
                    if words[j].startswith(words[i][k:]):
                        congruency[i][j] = size - k
                        break
    shortest_word = "".join(words)
    for i in range(n):
        l = recursive_find(i, 2**i)
        if len(l) <= len(shortest_word):
            shortest_word = l
    return shortest_word
   
def rev_palindrome(dna):
    ret = []
    for i in range(len(dna)):
        for j in range(i, len(dna)):
            if (j-i) <= 2 or (j-i) >= 10:
                continue
            elif reverse_complement(dna[i:j+1]) == dna[i:j+1]:
                ret.append((i,j-i+1))
    return ret
  
def reverse_complement(dna):
    dna = dna[::-1]
    revcomdna = ""
    complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
    for char in (dna):
        revcomdna += complements[char]
    return revcomdna

def get_edges(dna_dict):
    m1=[]
    for x,e1 in dna_dict.items():
        for c,e2 in dna_dict.items():
          if x!=c:
            if e1[-3:]==e2[:3]:
              m1.append((c,x))
    return m1

eqn = get_edges({"Rosalind_0498":"AAATAAA",
                 "Rosalind_2391":"AAATTTT",
                 "Rosalind_2323":"TTTTCCC",
                 "Rosalind_0442":"AAATCCC",
                 "Rosalind_5013":"GGGTGGG"})
            
