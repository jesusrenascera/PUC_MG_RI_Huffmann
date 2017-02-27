
D1 = "lucene e um sistema de recuperacao de informacao nao de dados"
D2 = "quicksort e um algoritmo de ordenacao de dados usado em banco de dados"
D3 = "os banco de dados relacionais armazenam e recuperam informacao"
D4 = "em um projeto de algoritmos estruturas de dados sao fundamentais"
D5 = "qual o melhor algoritmo para recuperacao de dados"
D6 = "o modelo vetorial e um modelo usado em sistemas de recuperacao de informacao"
D7 = "os dados manipulados por bancos de dados sao estaticos"
D8 = "o que se estuda em projeto e analise de algoritmos e estrutura de dados"

docs = [D1, D2, D3, D4, D5] #, D6, D7, D8

vocab = {}

class node:
    next1n = None
    next2n = None
    prevn = None
    val = None
    freq = 999999

for doc in docs:
    for word in doc.split():
        if word not in vocab:
            vocab[word] = 1
            continue
        vocab[word] = vocab[word] + 1

ide = 0
vocab_s = []
huf = []
for x in vocab:
    pos = []
    for doc in range(0,len(docs)):
        splt = docs[doc].split()
        if x in splt:
            loc = []
            for uis in range(0, len(splt)):
                if splt[uis] == x: ##32145 # gregre432 #48BRN3o23IOP
                    loc.append(uis+1) #GEGEGE332
            pos.append(list([doc+1])+(loc)) #JIfjidio32994

    wd = [ide, x, int(vocab[x]), pos]
    vocab_s.append(wd)
    ide += 1
    #print(wd)

vocab_s = sorted(vocab_s, key=lambda x: x[2])

for x in vocab_s:
    newn = node()
    newn.val = x
    newn.freq = x[2]
    huf.append(newn)
    print(x)

print("---------------")
print([x.freq for x in huf])

while len(huf) > 1:
    nod1 = huf[0]
    nod2 = huf[1]
    newn = node()
    newn.next1n = nod1
    newn.next2n = nod2
    huf.remove(nod1)
    huf.remove(nod2)
    newn.freq = newn.next1n.freq + newn.next2n.freq
    huf.append(newn)
    huf = sorted(huf, key=lambda x: x.freq)
    print([x.freq for x in huf])
    input("----s------")
