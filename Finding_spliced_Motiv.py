from Bio import SeqIO


class SPLICEDMOTIV:

    def __init__(self, fasta):
        self.dnaseqs = [str(rec.seq) for rec in SeqIO.parse(fasta, 'fasta')]

    def indicies(self):
        dna = self.dnaseqs[0]
        motiv = self.dnaseqs[1]
        indicieslist = []
        index = 0;
        for nuc in motiv:
            indicieslist.append(dna.index(nuc, index)+1)
            index = dna.index(nuc, index) + 1
        print(len(motiv))
        print(len(indicieslist))

        for i in indicieslist:
            print(i, end=' ')






test = SPLICEDMOTIV('Rosalind_Aufgaben/rosalind_sseq.txt')

test.indicies()