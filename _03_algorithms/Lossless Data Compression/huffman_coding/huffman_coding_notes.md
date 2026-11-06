# Huffman Coding 
Binary-Tree based method of generating reliable 
prefix-free codewords for characters 

## How to Encode using Huffman Coding 
```text
Requires:
1. Frequencies of Characters

Yields:
1. Shortest Codeword for the most frequent character 
2. second Shortest Codeword for the second most frequent character etc
```

### Huffman Code Tree Structure
+ binary tree 
+ each character to be encoded is represented by a leaf node 
+ each internal node denotes the subset of characters 
+ path/traversal from root node to any leaf yields a prefix-free binary 'codeword'




<span style="background-color: #FFF9C4; color: black; font-weight: bold;">
Huffman is a Greedy Algorithm</span>


