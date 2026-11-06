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

