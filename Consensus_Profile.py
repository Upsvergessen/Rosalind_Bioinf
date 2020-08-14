from Bio import SeqIO
from collections import Counter


class CONSENSUSSTRING:

    def __init__(self, fasta):
        self.seqs = [str(rec.seq) for rec in SeqIO.parse(fasta, 'fasta')]

    def constructmatrix(self):
        countseqs = []
        seq = ''
        for i in range(0, len(self.seqs[0])):
            for y in range(0, len(self.seqs)):
                seq += self.seqs[y][i]
            countseqs.append(seq)
            seq = ''
        matrix = {'A': [mini.count('A') for mini in countseqs], 'C': [mini.count('C') for mini in countseqs],
                  'G': [mini.count('G') for mini in countseqs], 'T': [mini.count('T') for mini in countseqs],
                  }

        string = ''
        for s in countseqs:
            string += Counter(s).most_common(1)[0][0]
        print(string)

        return matrix


test = CONSENSUSSTRING('Rosalind_Aufgaben/rosalind_cons.txt')
for k, v in test.constructmatrix().items():
    print(k + ': ' + str(v)[1:-1].replace(',', ''))
