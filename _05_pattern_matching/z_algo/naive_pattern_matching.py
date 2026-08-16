def naive_pattern_matching(str, pat, arr):
    """_summary_
    Time Complexity: O(nm), n: len(str), m: len(pat)
    Args:
        str (_type_): _description_
        pat (_type_): _description_
        arr (_type_): _description_
    """
    for i in range(len(str)): 
        for j in range(len(pat)):
            if str[i+j] != pat[j]: 
                break 
        if j == len(pat) - 1 and str[i+j] == pat[j]: 
            arr.append(i)