from Bio import SeqIO
import timeit


class SUPERSTRING:

    def __init__(self, fasta):
        self.dnaSeqs = [str(rec.seq) for rec in SeqIO.parse(fasta, 'fasta')]

    def generateGraph(self):

        graph = {}
        for seq1 in self.dnaSeqs:
            graph.__setitem__(seq1, [])
            for seq2 in self.dnaSeqs:
                if seq1 == seq2:
                    continue
                for i in range(min(len(seq1), len(seq2)), 0, -1):
                    if seq1[-i:len(seq1)] == seq2[0:i]:
                        graph[seq1].append((seq2, i))
                        break

        return graph

    def mergeseqs(self, graph):
        if len(list(graph.keys())) == 1:
            return graph.keys()

        kanten = []
        for edges in graph.values():
            kanten.extend(edges)
        kanten.sort(key=lambda x: x[1], reverse=True)
        bigest = kanten[0]
        override = ''
        oldkey = ''
        print(bigest)
        for ke in graph.keys():
            if bigest in graph[ke]:
                newkey = ke[0:-bigest[1]] + bigest[0]
                graph.__setitem__(newkey, graph[bigest[0]])
                print('New entry ')
                graph.pop(ke)
                graph.pop(bigest[0])
                override = newkey
                oldkey = ke
                break

        for ke in graph.keys():
            for edge in graph[ke]:
                if oldkey == edge[0]:
                    graph[ke].remove(edge)
                    graph[ke].append((override, edge[1]))
                    print('moinsen')

        return graph


def run():
    s = SUPERSTRING('Rosalind_Aufgaben/rosalind_long.txt')
    graph = s.generateGraph()
    for k, v in graph.items():
        print(k, v)

    while len(list(graph.keys())) > 1:
        graph = s.mergeseqs(graph)

    print(list(graph.keys()))


start = (timeit.default_timer())
print('Starttime '+ str(start))
run()
stop = timeit.default_timer()
print(stop-start)




