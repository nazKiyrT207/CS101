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
