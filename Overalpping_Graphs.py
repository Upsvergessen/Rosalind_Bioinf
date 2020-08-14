from Bio import SeqIO

class OVERLAPS:
    def __init__(self,fasta):
        self.table = {str(rec.seq): rec.id for rec in SeqIO.parse(fasta, 'fasta')}
        self.seqs = [seq for seq in self.table.keys()]


    def determine_overlaps(self, lenght):
        erg = []
        for seq1 in self.seqs:
            for seq2 in self.seqs:
                if seq1 == seq2:
                    continue
                if seq1[-lenght:] == seq2[:lenght]:
                    erg.append((self.table[seq1], self.table[seq2]))

        with open('Overlaps.txt', 'w')as f:
            for x in erg:
                f.write(x[0] + ' ' + x[1] + '\n')
        return erg



moinsen = OVERLAPS('Rosalind_Aufgaben/rosalind_grph.txt')
print(moinsen.table)
print(moinsen.seqs)

for x in moinsen.determine_overlaps(3):
    print(x[0] + ' '+ x[1])
