class Node:
    def __init__(self, text, frequency):
        self.text = text
        self.frequency = frequency
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, tree_root_note, text):
        self.tree_root_note = tree_root_note
        self.text = text

class HuffmanCoding:
    def __init__(self, text: str):
        self.text = text
        self.frequency = {}
        self.codes = {}
        self.root = None
        self.trees = []

    def get_text(self):
        return self.text

    def get_frequency(self):
        return self.frequency

    def get_codes(self):
        return self.codes

    def get_root(self):
        return self.root

    def calculate_frequency(self):
        """
        Function to calculate the frequency of each character in the text
        Time Complexity: O(n + klogk), where n is the length of the text, klogk is the time taken to sort the frequency dictionary
        Space Complexity: O(k), where k is the number of unique characters in the text
        Returns: None
        """
        for char in self.text:
            if char not in self.frequency:
                self.frequency[char] = 1
            else:
                self.frequency[char] += 1

        self.frequency = sorted(self.frequency.items(), key=lambda item: item[1]) # O(klogk) - TimSort

    def build_huffman_tree(self):
            while len(self.frequency) != 0:
                iteration_count = 1
                node_text = ""
                new_node = Node(node_text, 0)
                new_node_freq = 0

                while iteration_count >= 0:
                    # print(f"Iteration {iteration_count}")
                    # print(self.frequency[iteration_count])
                    node_text = self.frequency[iteration_count][0] + node_text
                    new_node_freq += self.frequency[iteration_count][1]
                    root_node_found = False
                    for root_node in self.trees:
                        if self.frequency[iteration_count][0] == root_node.text:
                            if new_node.right is None:
                                new_node.right = root_node
                            else:
                                new_node.left = root_node
                            root_node_found = True

                    if not root_node_found:
                        if new_node.right is None:
                            new_node_right = Node(self.frequency[iteration_count][0], self.frequency[iteration_count][1])
                            new_node.right = new_node_right
                        else:
                            new_node_left = Node(self.frequency[iteration_count][0], self.frequency[iteration_count][1])
                            new_node.left = new_node_left

                    self.frequency.pop(iteration_count)
                    print(self.frequency)

                    iteration_count -= 1

                # print(f"node_text={node_text}, new_node_freq={new_node_freq}")
                new_node.text = node_text
                new_node.frequency = new_node_freq
                # print(f"new_node.text={new_node.text}, new_node.frequency={new_node.frequency}, new_node.left={new_node.left.text}, new_node.right={new_node.right.text}")
                new_tree_root = new_node
                self.root = new_tree_root
                self.trees.append(new_tree_root)

                # add the new_tree_root text to the self.frequency list
                if len(self.frequency) == 0:
                    break
                self.frequency.append((new_node.text, new_node.frequency))

                self.frequency = sorted(self.frequency, key=lambda item: item[1])
                # print(f"self.frequency2={self.frequency}")

            print(self.get_root().text)



    def letter_encoding(self, node, code="", encoded_letter=None):
        # get the coding for each letter, by traversing from root down to leaf
        if encoded_letter is None:
            encoded_letter = {}
        if node is None:
            return encoded_letter

        if node.left is None and node.right is None:
            encoded_letter[node.text] = code
            return encoded_letter

        self.letter_encoding(node.left, code + "0", encoded_letter)
        self.letter_encoding(node.right, code + "1", encoded_letter)

        return encoded_letter

    def encode(self):
        encoded_letter = self.letter_encoding(self.root)
        print(encoded_letter)
        encoded_stream=""

        for letter in self.text:
            encoded_stream+=encoded_letter[letter]

        return encoded_stream

    def decoding(self):
        pass


if __name__ == '__main__':
    huffman_coding = HuffmanCoding(text="A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED")
    huffman_coding.calculate_frequency()
    print(huffman_coding.get_frequency())
    huffman_coding.build_huffman_tree()
    encoded_stream = huffman_coding.encode()
    print(encoded_stream)
