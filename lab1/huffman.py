def readData(filename):
    f=open(filename)
    data=f.readline()
    dict={}
    for i in range(0,len(data)):
        if data[i] in dict:
            dict[data[i]]=dict[data[i]]+1
        else:
            dict[data[i]]=1
    return dict

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq=freq
        self.symbol=symbol
        self.left=left
        self.right=right
        self.huff=''

def printNodes(node, val=''):
    global list
    newVal=val+str(node.huff)
    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)
    if (not node.left and not node.right):
        print(str(node.symbol)+": "+str(newVal))
        list[str(node.symbol)]=str(newVal)

def codify(text,list):
    code=""
    for symbol in text:
        code=code+list[symbol]
    return code

def decodify(text,list):
    decoded=""
    i=0
    while i<len(text):
        j=i+1
        while 1:
            string=text[i:j]
            ok=0
            for key,value in list.items():
                if value == string:
                    decoded=decoded+key
                    i=j-1
                    ok=1
                    break
            if ok == 1:
                break
            j=j+1
        i=i+1
    return decoded

def huffman_tree(freq):
    nodes = []
    for x in freq:
        nodes.append(node(x[1], x[0]))
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes[0]
        right = nodes[1]
        left.huff = 0
        right.huff = 1
        newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    return nodes

dict=readData("huffman.in")
nodes_aux=sorted(dict.items(), key=lambda item: item[1])
nodes=huffman_tree(nodes_aux)
list={}
printNodes(nodes[0])
print(codify("aabacdab",list))
print(decodify("00100110111010",list))
f=open("t8.shakespeare.codify.txt",'w')
f.write(codify("aabacdab",list))
f.close()