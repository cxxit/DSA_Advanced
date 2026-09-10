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

def boyer_moore(txt, pat):
    rightmost_occ_arr = preprocess_bad_char_shift_data_structure_extended(pat) 
    j_start = 0
    j = j_start + len(pat) - 1 
    i = len(pat) - 1

    while j < len(txt):
        while i>=0:
            if txt[j] != pat[i]: 
                break
            j -= 1
            i -= 1
        if i >= 0: 
            mistmatch_index_txt = j_start + i
            mistmach_letter_txt = txt[mistmatch_index_txt]
            r_x = rightmost_occ_arr[i][ord(mistmach_letter_txt)-97] # 97 = ord("a")

            shift_amount = extended_bad_char_shift_rule(i,r_x, len(pat))
            j_start = j_start + shift_amount
            j = j_start + len(pat) - 1 
            i = len(pat) - 1
        else: # i == -1
            return "full match found"
    return "no pat found in txt"


def boyer_moore():
   pass


if __name__ == "__main__": # runs when you run this python file directly, but not when the file is imported as a module
    txt = "abcdefheheheheehxyz"
    pat = "xyz"
    print(bad_char_shift_rule(txt, pat))

