import heapq
import json
from heapq import heappop, heappush
 
def isLeaf(root):
    return root.left is None and root.right is None
 
class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq
 
 
# tworzenie kodów huffmana (kodowanie)
def encode(root, str, huffman_code):
 
    if root is None:
        return
 
    if isLeaf(root):
        huffman_code[root.ch] = str if len(str) > 0 else '1'
 
    encode(root.left, str + '0', huffman_code)
    encode(root.right, str + '1', huffman_code)
 
 
#  dekododowanie kodów huffmana
def decode(root, index, str):
 
    if root is None:
        return index
 
    if isLeaf(root):
        print(root.ch, end='')
        return index
 
    index = index + 1
    root = root.left if str[index] == '0' else root.right
    return decode(root, index, str)
 
# tworzenie kolejki
def queue(freq):
    q = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(q)
 
    # jezeli jest wiecej niz jeden node w kolejce
    while len(q) != 1:
 
        # usuń dwa node z najwyzszym priorytetem (najmniejsza liczba wystapien) z kolejki
 
        left = heappop(q)
        right = heappop(q)
 
        # tworzenie nowego wewnetrznego node z dwoma nodami jako dzieci i z iloscia wstapien rowna sumie wystapien w dzieciach
        total = left.freq + right.freq
        heappush(q, Node(None, total, left, right))
    return q
 
# Tworzenie drzewa Huffmana i dekodowanie podanego tekstu
def buildHuffmanTree(text):
    # jezeli przekazano pusty tekst
    if len(text) == 0:
        return
 
    #tworzenie slownika charów i liczby ich wystąpień
    freq = { char: text.count(char) for char in set(text) }
    q = queue(freq)
 
    # główny node
    root = q[0]
 
    # przejście po drzewie i utworzenie kodów Huffmana
    huffmanCode = {}
    encode(root, "", huffmanCode)
 
    # utworzenie zakodowanego ciągu
    str = ""
    for c in text:
        str += huffmanCode.get(c)
    
    # słownik z wynikiem - zakodowany ciąg + liczba wystąpień znaków
    result = dict()
    result['encoded'] = str
    result['freq'] = freq
    return  result
   
 
def decodeFromFile(root, str):
    # przejście po drzewie w celu zdekodowania ciągu
    index = -1
    while index < len(str) - 1:
        index = decode(root, index, str)

# MAIN === Algorytm Huffmana ==== 
text = "Huffman coding sample text."
result = buildHuffmanTree(text)

encoded = result['encoded']
freq = result['freq']

print("The encoded string is:", encoded)

# Zapisujemy do plików zakodowany ciąg i liczbe wystąpień poszczególnych znaków
f = open("huffmanEncoded.txt", "w")
f.write(encoded)
f.close()

f = open("huffmanFreq.txt", "w")
f.write(json.dumps(freq))
f.close()


# Odczytujemy z plików zakodowany ciąg i liczbe wystąpień poszczególnych znaków
f = open("huffmanEncoded.txt", "r")
encodedFromFile = f.read()
f.close()

f = open("huffmanFreq.txt", "r")
freqFile = f.read()
freqFromFile = json.loads(freqFile)
f.close()

# Tworzymy kolejkę na podstawie danych z plików i dekodujemy tekst
q = queue(freqFromFile)
print("The decoded string is:", end=' ')
decoded = decodeFromFile(q[0], encodedFromFile)