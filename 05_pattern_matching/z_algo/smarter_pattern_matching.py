# str = "aaachibbxchbchin"
# str = "chinchinchinchin"
# pat = "chin"

str = "xabxyabxyabxz"
pat = "qqqqq"
def smarter_pattern_matching(str, pat, arr): 
    i = 0
    next_start_index = None
    while i < len(str):
        for j in range(len(pat)): 
            if str[i+j] == pat[0]:
                next_start_index = i + j
            if str[i+j] != pat[j]: 
                break 

        if j == len(pat) - 1 and pat[j] == str[i+j]: 
            arr.append(i)

        if next_start_index:
            if j > next_start_index: 
                i = next_start_index
            else: 
                i = i + j + 1
        else: 
            i += 1

    return arr

print(smarter_pattern_matching(str, pat, []))





