import itertools as it


def convert(liste):
    return [-i for i in liste]




def signedpermutations(zahl):
    p = it.permutations(range(1, zahl+1))
    permlist = [list(perm) for perm in p]
    result = [el for el in permlist]
    print(len(result)*2**zahl)

    for pem in permlist:
        for i in range(1,zahl+1):
            newelement = []
            for c in range(0,len(pem)+1-i):
                if c == 0:
                    newelement = convert(pem[c:c+i]) + pem[c+i:]
                    result.append(newelement)
                else:
                    newelement = pem[:c] + convert(pem[c:c+i]) + pem[c+i:]
                    result.append(newelement)
    print(len(result))
    for r in result:
        for i in r:
            print(str(i) + ' ', end='')
        print()

def checkpermutation(permutation):
    permutation = list(map(abs, permutation))
    if len(permutation) == len(set(permutation)):
        return True
    return False

def signedperm2(zahl):
    zahlen = list(range(-zahl,0)) + list(range(1,zahl+1))
    p = it.permutations(zahlen, zahl)
    perms = [comb for comb in p if checkpermutation(comb)]


    with open('permutations.txt', 'w') as f:
        f.write(str(len(perms)) + '\n')
        for i in perms:
            for z in i:
                f.write(str(z) + ' ')
            f.write('\n')


signedperm2(5)
