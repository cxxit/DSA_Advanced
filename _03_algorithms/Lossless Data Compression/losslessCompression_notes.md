# Lossless Data Compression 
## What is Compression 
*Definition:* Practice of representing information in a **compact form**
```text
Compression is achieved by identifying and exploiting repeat-patterns in data

Data = redundant parts + random parts
     = compressible parts + uncompressible parts 
     = model + deviations 
     = signal + noise  
```

## What does Compression do? 
Saves **space** and **time**

## What is Lossless Compression
*Definition:* algorithms that allow us to encode the original data into a compact (encoded) form, can is able to turn back perfectly (decoded) to get original data back


## Fixed-Length Codeword 
ASCII 

## Variable-Length Codeword
````text
Example: Morse Code
- may reduce the total number of bits 
    - as frequent symbols are assigned shorter codewords
    - infrequent symbols assigned longer codewords

Problem: decoding becomes ambiguous    

A =0, B=1, C=10, D=101 
BABA = 1010 
1010 could be interpreted as 
    -DA
    -BAC 
    -CC
    -CBA
    
    
However ensuring that the CodeWord is prefix-free removes the ambiguity 
````

