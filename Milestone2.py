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
