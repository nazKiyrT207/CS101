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

def rev_palindrome(dna):
   result= []
   for i in range(len(dna)-4):
     z = min(len(dna),i+12)
     for j in range(i+3,z):
           word = dna[i:j+1]
           if (reverse_complement(dna[i:j+1]) == word):
               result.append((i,j-i+1))
   return result
   
