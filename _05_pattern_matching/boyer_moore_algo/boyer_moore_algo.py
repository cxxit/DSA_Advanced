# Strucutre of Boyer Moore Algorithm 
    # Proprocessing phase (performed once at the start of the algo):
        # preprocess pat to obtain 3 data structures to support each shift rule 
            # bad character shift rule data structures
            # -> preprocess pat to store for each character in sigma the rightmost position of the occurence of character x in pat
            # store position R(x) 
            # when x does not occur in pat R(x) = 0 
def preprocess_bad_char_shift_data_structure(pat): 
    """_summary_
    Space Complexity: O(|Sigma|), rightmost_arr, stores sigma length, where sigma denotes number of alphabet
    Time Complexity: O(m + |Sigma|), depending on the length of the pat and the number of alphabet, 
                     total time to store 0 in rightmost_arr and total time to compute frequency of each letters in the patter
    Args:
        pat (_type_): _description_
    """
    rightmost_arr = [None] * 26 # there is 26 letters in english language, Space Complexity: O(|Sigma|)

    for i in range(len(pat)):
    # for letter in pat: 
        letter_index = ord(pat[i]) - 97
        # print(letter_index)
        rightmost_arr[letter_index] = i # this updates the arr to store the right most position of each letter in pat 

    return rightmost_arr

def bad_char_shift_rule(txt, pat): 
    """Implementation of Bad Character Shift Rule
    1. Right to left scan until a mismatch is found

    """
    rightmost_occ_arr = preprocess_bad_char_shift_data_structure(pat) 
    mismatch = False
    j_start = 0
    j = j_start + len(pat) - 1 
    i = len(pat) - 1

    while j_start < len(txt):
        # for hehe in range(20):
        # while j>=0 and i>=0 and mismatch == False:
        while i>=0:
            if txt[j] != pat[i]: 
                mismatch = True 
                print(txt[j], pat[i], f"mismatch at k (index at pat): {i}, x (index at txt): {j_start + i}")
                break
            print(txt[j], pat[i])
            j -= 1
            i -= 1
        if i >= 0 and mismatch == True: 
        # get r_x value, r_x represents right most index of letter x in pat 
        # 1. we need to know the letter in txt which mistmatch occured 
            # get letter in txt which mismatch occured 
            mistmatch_index = j_start + i
            print(mistmatch_index,"mismatch index")
            mistmach_letter_txt = txt[mistmatch_index]
            r_x = rightmost_occ_arr[ord(mistmach_letter_txt)-97] # 97 = ord("a")
            print(rightmost_occ_arr)
            print(ord(mistmach_letter_txt)-97, mistmach_letter_txt, r_x)
            if r_x == None: 
                j_start = j_start + len(pat)
                
            # do a shift using the r_x
            elif r_x < i:
                print(j_start + i - r_x, "new_j_start")
                if j_start + r_x > len(txt) - 1 or j_start + i - r_x + len(pat) - 1 > len(txt) - 1: 
                    return "no pat found in txt"
                j_start = j_start + i - r_x
            else: 
                j_start = j_start + 1
            j = j_start + len(pat) - 1 
            i = len(pat) - 1
            mismatch = False

        else: # i is less than zero denotes that a full match is found
            return "full match found"

    return "no pat found in txt"
        

def boyer_moore():
   pass


if __name__ == "__main__": # runs when you run this python file directly, but not when the file is imported as a module
    txt = "abcdefheheheheehxyz"
    pat = "xyz"
    print(bad_char_shift_rule(txt, pat))

