def find_splice(dna_motif, dna):
  start = 0
  li = []
  for i in dna_motif:
    li.append(dna.index(i, start))
    start = dna.index(i, start)
  return li
