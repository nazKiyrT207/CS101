def find_splice(dna_motif, dna):
  start = 0
  li = []
  for i in dna_motif:
    li.append(dna.index(i, start+1))
    start = dna.index(i, start)
  return li
