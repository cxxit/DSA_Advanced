def preprocess_bad_char_shift_data_structure_extended(pat): 
    rightmost_matrix = [] # initialise matrix
    rightmost_arr = [None] * 26 # initialise rightmost_arr storing rightmost index of each character in pat
    rightmost_matrix.append(rightmost_arr) # append initial rightmost_arr as at index 0, no characters is to the left of the character at index 0
    for i in range(1,len(pat)):
        rightmost_arr = [None] * 26
        for j in range(0,i): 
            letter = pat[j]
            letter_index = ord(letter) - 97
            rightmost_arr[letter_index] = j
        rightmost_matrix.append(rightmost_arr)
    return rightmost_matrix


def extended_bad_char_shift_rule(i, r_x, pat_length): 
    """
    j: current index traversing in txt
    i: current index traversing in pat

    Args:
        pat (_type_): _description_
def good_suffix_shift_arr(pat): 
    # initialise the array with 
    good_suffix_arr = [0] *  (len(pat) + 1)

    z_suffix_arr = computeZSuffixValues(pat)

    for p in range(len(good_suffix_arr) - 2): 
        j = len(pat) - z_suffix_arr[p] + 1  - 1 # minus one to make it zero indexing
        good_suffix_arr[j] = p
    return good_suffix_arr # goodsuffix arr is based on zero based indexing

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
            else: # shift naively 
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

