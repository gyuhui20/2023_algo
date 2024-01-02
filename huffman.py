__license__ = 'Junior (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: huffman.py 2023-03-24'

"""
Huffman homework
2023-03
@author: gyuhui.kwon
"""

from algo_py import bintree
from algo_py import heap


###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

###############################################################################
## COMPRESSION

def build_frequency_list(dataIN):
    """
    Builds a tuple list of the character frequencies in the input. 
    """
    itemList, countList, freqList = [], [], []
    for char in dataIN:
        if char not in itemList:
            itemList.append(char) 
            count = 0 
            for char2 in dataIN: 
                if char == char2:
                    count += 1 
            countList.append(count) 
    for i in range(len(itemList)): 
        freqList.append((countList[i], itemList[i]))
    return freqList


def build_Huffman_tree(inputList):
    """
    Processes the frequency list into a Huffman tree according to the algorithm. 
    """
    HT = [] 
    for i in range(len(inputList)): 
        HT.append([inputList[i][0], bintree.BinTree(inputList[i][1], None, None)])
    while len(HT) != 1:
        length = len(HT) - 1
        for i in range(length):
            isSort = False
            for j in range(length - i):
                if(HT[j][0] < HT[j+1][0]): 
                    HT[j], HT[j+1] = HT[j+1], HT[j]
                    isSort = True
            if isSort == False:
                break
        mergedTree = [HT[-1][0] + HT[-2][0], bintree.BinTree(None, HT[-1][1], HT[-2][1])]
        HT.pop()
        HT.pop()
        HT.append(mergedTree)
    return HT[0][1]


def __search_occ2(B, x) :  
    if B.left == None : 
        if B.key == x : 
            return "" 
        else : 
            return None 
    else :
        res = __search_occ2(B.left, x)
        if res != None : 
            return '0' + res 
        else :
            res = __search_occ2(B.right, x)
            if res != None : 
                return '1'+ res
            else :
                return None

def __search_occ(B,x) :
    if B == None :
        return None
    else :
        return __search_occ2(B,x)        


def encode_data(huffmanTree, dataIN):
    """
    Encodes the input string to its binary string representation.
    """
    encode = ''
    for i in range(len(dataIN)) : 
        x = dataIN[i]
        encode+=(__search_occ(huffmanTree, x))
    return encode


def __decimal_to_binary1(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

def __decimal_to_binary(decimal) :
    if len(__decimal_to_binary1(decimal)) <= 7:
        return "0"*(8-len(__decimal_to_binary1(decimal))) + __decimal_to_binary1(decimal)
    else :
        return __decimal_to_binary1(decimal)

def __encode_tree_recursive(huffmanTree, resultList, leftCount=0):
    if huffmanTree.key == None:
        __encode_tree_recursive(huffmanTree.left, resultList, leftCount+1)
        __encode_tree_recursive(huffmanTree.right, resultList)
    else:
        encodedKey = "0"*leftCount + "1" +__decimal_to_binary(ord(huffmanTree.key))
        resultList.append(encodedKey)

def encode_tree(huffmanTree):
    """
    Encodes a huffman tree to its binary representation using a preOrder traversal:
        * each leaf key is encoded into its binary representation on 8 bits preceded by '1'
        * each time we go left we add a '0' to the result
    """
    encodedKeyList = []
    __encode_tree_recursive(huffmanTree, encodedKeyList)
    encodedTree = ""
    for encodedKey in encodedKeyList:
        encodedTree += encodedKey 
    return encodedTree


def to_binary(dataIN):
    """
    Compresses a string containing binary code to its real binary value.
    """
    dataComp = "" 
    align = 8-len(dataIN)%8 
    for i in range(0,len(dataIN)-align,8) : 
        binary_num = dataIN[i:i+8] 
        decimal_num = 0 
        for j in range(8):
            decimal_num += int(binary_num[j]) * 2**(8-j-1)
        dataComp += chr(decimal_num)
    if align != 0 : 
        binary_num2 = "0" * (align) + dataIN[-(8-align):]
        decimal_num = 0
        for j in range(8):
            decimal_num += int(binary_num2[j]) * 2**(8-j-1)
        dataComp += chr(decimal_num)
    return (dataComp, align)


def compress(dataIn):
    """
    The main function that makes the whole compression process.
    """
    freqList = build_frequency_list(dataIn)
    HT = build_Huffman_tree(freqList)
    encData = encode_data(HT, dataIn) 
    encTree = encode_tree(HT)
    (dataComp, align) = to_binary(encData)
    (treeComp, alignTree) = to_binary(encTree)
    return (dataComp, align), (treeComp, alignTree)


################################################################################
## DECOMPRESSION

def decode_data(huffmanTree, dataIN):
    """
    Decode a string using the corresponding huffman tree into something more readable.
    """
    decData = ''
    tree = huffmanTree
    for i in range(len(dataIN)) :
        bit = dataIN[i]
    for bit in dataIN :
        if bit == '0': 
            tree = tree.left 
        else: 
            tree = tree.right 
        if tree.key is not None: 
            decData += tree.key
            tree = huffmanTree    
    return decData 

    
def decode_tree(dataIN):
    """
    Decodes a huffman tree from its binary representation:
        * a '0' means we add a new internal node and go to its left node
        * a '1' means the next 8 values are the encoded character of the current leaf         
    """
    # FIXME
    pass


def from_binary(dataIN, align):
    """
    Retrieve a string containing binary code from its real binary value (inverse of :func:`toBinary`).
    """
    binary =''
    for i in range(len(dataIN)-1) :
        decimal = ord(dataIN[i])
        binary += __decimal_to_binary(decimal)
    decimal_ = ord(dataIN[-1])
    binary += __decimal_to_binary(decimal_)[-(8-align):]
    return binary


def decompress(data, dataAlign, tree, treeAlign):
    """
    The whole decompression process.
    """
    dataIN = from_binary(tree, treeAlign)
    HT = decode_tree(dataIN)
    encData = from_binary(data, dataAlign)
    decode = decode_data(HT, encData)
    return decode

