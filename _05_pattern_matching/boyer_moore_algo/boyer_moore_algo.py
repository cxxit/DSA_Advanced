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


def extended_bad_char_shift_rule(i, r_x): 
    """
    j: current index traversing in txt
    i: current index traversing in pat

    Args:
        txt (_type_): _description_
        pat (_type_): _description_

    Returns:
        _type_: _description_
    """
    print(f"inside function r_x: {r_x}")
    if r_x == None: # if the letter mismatched in the txt is not in the pat, we shift the len(pat)
        shift_amount = i + 1

    else:
        shift_amount = i - r_x

    return shift_amount

def computeZSuffixValues(pat): 
    z_value_arr = [] 
    reverse_pat = ""
    for i in range(len(pat)-1,-1,-1):
        reverse_pat += pat[i]
    # print(f"reverse_pat: {reverse_pat}")

    # use gusfield algo on the reversed pattern 
    z_value_arr.append(len(pat))
    # print(f"first instance of z_suffix_arr:{z_value_arr}")
    i = 0
    current_index = 1
    j = current_index
    while current_index < len(reverse_pat): 
        count = 0
        i = 0
        j = current_index
        # print(f"current index: {current_index}")
        # print(f"i: {i}, Scurrent index: {current_index}, j: {j}, {reverse_pat}, {reverse_pat[j]}")
        while j < len(reverse_pat): 
            # print(f"reverse_pat[i] == reverse_pat[j]: {reverse_pat[i] == reverse_pat[j]}")
            if reverse_pat[i] == reverse_pat[j]:
                count += 1
                j += 1 
                i += 1
            else: 
                break
        z_value_arr.append(count)
        current_index += 1

    # reverse the values in the z_value_arr
    z_suffix_arr = []
    for i in range(len(z_value_arr)-1,-1,-1): 
        z_suffix_arr.append(z_value_arr[i])
    z_suffix_arr.append(None)
    return z_suffix_arr


def good_suffix_shift_arr(pat): 
    # initialise the array with 
    good_suffix_arr = [0] *  (len(pat) + 1)

    z_suffix_arr = computeZSuffixValues(pat)

    for p in range(len(good_suffix_arr) - 2): 
        j = len(pat) - z_suffix_arr[p] + 1  - 1 # minus one to make it zero indexing
        good_suffix_arr[j] = p
    return good_suffix_arr # goodsuffix arr is based on zero based indexing

def matched_prefix_shift_arr(pat): 
    z_suffix_arr = computeZSuffixValues(pat)
    print(z_suffix_arr)

    # obtain matched prefix 
    matched_prefix_shift_arr_unreversed = []
    largest_value = z_suffix_arr[0] # initialise largest value as first element in z_suffix_arr
    for i in range(len(z_suffix_arr) - 1): 
        if z_suffix_arr[i] > largest_value: 
            largest_value = z_suffix_arr[i]
        matched_prefix_shift_arr_unreversed.append(largest_value)
    matched_prefix_shift_arr = []
    for j in range(len(matched_prefix_shift_arr_unreversed)-1,-1,-1): 
        matched_prefix_shift_arr.append(matched_prefix_shift_arr_unreversed[j])
    matched_prefix_shift_arr.append(0)

    return matched_prefix_shift_arr

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



if __name__ == "__main__": # runs when you run this python file directly, but not when the file is imported as a module
    # txt = "abcdefzxyz"
    # pat = "xyz"
    # print(boyer_moore(txt, pat))
    # preprocess_bad_char_shift_data_structure("hehe")
    # print(preprocess_bad_char_shift_data_structure_extended("tbapxb"))
    # print(computeZSuffixValues("abaaabacbaabaaab"))
    print(matched_prefix_shift_arr("acababacaba"))

