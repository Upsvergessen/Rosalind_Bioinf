def reverseComplement(dna):
    rna = dna.translate(dna.maketrans('ATCG','UAGC'))
    print([rna[n:n+3] for n in range(0,rna.__len__(),3)])




reverseComplement('GTTCTACATGAAACGTGTTCTCTCCTAGGGTAGACACGCTGAACTTGC')