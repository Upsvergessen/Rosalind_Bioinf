# Transition A > G ; T > C
# Transversion A > T ; G> C
from Bio import SeqIO


def transition_transversion_ratio(path):
    dnaseqs = [str(rec.seq) for rec in SeqIO.parse(path, 'fasta')]
    basedict = {'A': 'purine',
                'G': 'purine',
                'T': 'pyrimidin',
                'C': 'pyrimidin'}
    transitions = 0
    transversions = 0
    for x,y in zip(dnaseqs[0],dnaseqs[1]):
        if x != y:
            if basedict[x] == basedict[y]:
                transitions += 1
            else:
                transversions += 1

    return transitions/transversions

print(transition_transversion_ratio('Rosalind_Aufgaben/rosalind_tran.txt'))