import sys


class Huffman:
    def __init__(self, string):
        self.string = string

    def freq_dict(self):
        # Make a dictionary to count frequency of character
        frequency = {}
        for char in self.string:
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1
        return frequency

    def freq_sort(self):
        # Make a list of tuple sorted
        freq_sorted = []
        for key, value in self.freq_dict().items():
            freq_sorted.append(tuple((value, key)))
        freq_sorted.sort()
        return freq_sorted

    def huffman_tree(self):
        # Built the huffman tree
        tuples = self.freq_sort()
        if len(tuples) == 1:
            tuples.append((0, '\0'))
        while len(tuples) > 1:
            least_use_02 = tuple(tuples[0:2])
            remaining = tuples[2:]
            add_node = least_use_02[0][0] + least_use_02[1][0]
            tuples = remaining + [(add_node, least_use_02)]
            tuples.sort(key=lambda x: x[0])
        return tuples[0]

    def huffman_trim(self, tree):
        # Trim the freq counters off, leaving just the letters
        p = tree[1]                             # ignore freq count in [0]
        if type(p) == type(""):                 # if just a leaf (letter), return it
            return p
        else:
            return self.huffman_trim(p[0]), self.huffman_trim(p[1])  # trim left then right and recombine


def huffman_code(node, pat=''):
    # Assign binary code to characters(leaves)
    # It gets parameter node from huffman_trim
    global codes

    if type(node) == type(""):
        codes[node] = pat
    else:
        huffman_code(node[0], pat+"0")   # Branch point. Do the left branch
        huffman_code(node[1], pat+"1")   # then do the right branch
    return codes


def huffman_encoding(data):
    # Encode the text into its compressed form
    global codes
    output = ""
    for ch in data:
        output += codes[ch]
    return output


def huffman_decoding(data, tree):
    # Decode the text from its compressed form
    output = ""
    p = tree
    for bit in data:
        if bit == '0':
            p = p[1][0]
        else:
            p = p[1][1]
        if type(p[1]) == type(""):
            output += p[1]
            p = tree
    return output


if __name__ == "__main__":
    codes = {}
    a = int(input("Choose Test case #: "))
    if a == 1:
        a_great_sentence = "The bird is the word"
    elif a == 2:
        a_great_sentence = "AAAAAA"
    elif a == 3:
        a_great_sentence = ""

    if len(a_great_sentence) == 0:
        print("No data to encode")

    else:
        print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print("The content of the data is: {}\n".format(a_great_sentence))

        Huffman = Huffman(a_great_sentence)
        tree = Huffman.huffman_tree()
        trim_tree = Huffman.huffman_trim(tree)
        codes = huffman_code(trim_tree)

        encoded_data = huffman_encoding(a_great_sentence)
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)
        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the decoded data is: {}\n".format(decoded_data))




