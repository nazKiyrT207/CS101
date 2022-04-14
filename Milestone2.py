def rev_palindrome(dna):
   result= []
   for i in range(len(dna)-4):
     z = min(len(dna),i+12)
     for j in range(i+3,z):
           word = dna[i:j+1]
           if (reverse_complement(dna[i:j+1]) == word):
               result.append((i,j-i+1))
   return result
   
