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

