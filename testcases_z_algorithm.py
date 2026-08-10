from typing import List
import string, random, time


def z_algo(string: str) -> List[int]:
    """Implements Gusfield's Z-Algorithm to compute the z-values of a given string

    Args:
        string (str): The string to compute z-values for

    Returns:
        List[int]: A list of length len(string), with each index i corresponding to
                the z_i-value of the input string. First index is always None
    """
    n = len(string)
    z_arr = [0] * n
    r_arr = [0] * n
    l_arr = [0] * n

    # initialise first ith character to have len(string) as the z_value 
    z_arr[0] = len(string)

    # BASE CASE 
    for i in range(1,len(string)): 
        # print("i_value", i, "letter", string[i])
        if i > r_arr[i-1]: # Case 1 
            # pri/nt("Case 1")
            z_value = 0
            compare_index = 0 # starting index from first character in the string
            k=i
            while k<len(string) and compare_index<len(string) and string[k] == string[compare_index]:
                z_value += 1
                compare_index +=1 
                k += 1
            if z_value > 0: 
                l_value = i
                # r_value = k-1
                r_value = l_value + z_value - 1
            else: 
                l_value = l_arr[i-1]
                r_value = r_arr[i-1]
        else: 
            if z_arr[i-l_arr[i-1]+1-1] < r_arr[i-1]-i+1: # add -1 to the z_arr index as python starts from index 0
                # print("Case 2a", z_arr[i-l_arr[i-1]+1],  r_arr[i-1]-i+1)
                z_value = z_arr[i-l_arr[i-1]+1-1] # removed the + 1 is this correct
                l_value = l_arr[i-1]
                r_value = r_arr[i-1]

            else: 
                # print("Case 2b")
                z_value = 0
                compare_index = 0
                k=i
                while k<len(string) and compare_index<len(string) and string[k] == string[compare_index] :
                    z_value += 1
                    compare_index +=1 
                    k += 1
                r_value = k-1
                l_value = i
        # print("z_value", z_value, "r_value", r_value, "l_value", l_value)
        # print()
                

        z_arr[i] = z_value
        l_arr[i] = l_value
        r_arr[i] = r_value
    return z_arr
    


def test_z_alg() -> None:    
    word="acbaa"
    expected = [None, 0, 0, 1, 1]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for acbaa!\n\tExpected:[None, 0, 0, 1, 1]\n\tActual  :{z_algo(word)}")

    word="bbacbbabab"
    expected = [None, 1, 0, 0, 3, 1, 0, 1, 0, 1]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for bbacbbabab!\n\tExpected:[None, 1, 0, 0, 3, 1, 0, 1, 0, 1]\n\tActual  :{z_algo(word)}")

    word="acbacbccbababacbccba"
    expected = [None, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 1, 0, 3, 0, 0, 0, 0, 0, 1]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for acbacbccbababacbccba!\n\tExpected:[None, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 1, 0, 3, 0, 0, 0, 0, 0, 1]\n\tActual  :{z_algo(word)}")

    word="babbbabccbacccbbaacb"
    expected = [None, 0, 1, 1, 3, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for babbbabccbacccbbaacb!\n\tExpected:[None, 0, 1, 1, 3, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1]\n\tActual  :{z_algo(word)}")

    word="bccaacaccb"
    expected = [None, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for bccaacaccb!\n\tExpected:[None, 0, 0, 0, 0, 0, 0, 0, 0, 1]\n\tActual  :{z_algo(word)}")

    word="bccbcccbaacaabacccac"
    expected = [None, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for bccbcccbaacaabacccac!\n\tExpected:[None, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]\n\tActual  :{z_algo(word)}")

    word="ccbbababca"
    expected = [None, 1, 0, 0, 0, 0, 0, 0, 1, 0]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for ccbbababca!\n\tExpected:[None, 1, 0, 0, 0, 0, 0, 0, 1, 0]\n\tActual  :{z_algo(word)}")

    word="acccbcbcca"
    expected = [None, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for acccbcbcca!\n\tExpected:[None, 0, 0, 0, 0, 0, 0, 0, 0, 1]\n\tActual  :{z_algo(word)}")

    word="abcaabcaac"
    expected = [None, 0, 0, 1, 5, 0, 0, 1, 1, 0]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for abcaabcaac!\n\tExpected:[None, 0, 0, 1, 5, 0, 0, 1, 1, 0]\n\tActual  :{z_algo(word)}")

    word="bbcccbabbaccbcbcacab"
    expected = [None, 1, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for bbcccbabbaccbcbcacab!\n\tExpected:[None, 1, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1]\n\tActual  :{z_algo(word)}")

    word="acacbcbbabcbaca"
    expected = [None, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 1]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for acacbcbbabcbaca!\n\tExpected:[None, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 1]\n\tActual  :{z_algo(word)}")

    word="cbbcaaccccbbccb"
    expected = [None, 0, 0, 1, 0, 0, 1, 1, 1, 4, 0, 0, 1, 2, 0]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for cbbcaaccccbbccb!\n\tExpected:[None, 0, 0, 1, 0, 0, 1, 1, 1, 4, 0, 0, 1, 2, 0]\n\tActual  :{z_algo(word)}")

    word="bbabc"
    expected = [None, 1, 0, 1, 0]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for bbabc!\n\tExpected:[None, 1, 0, 1, 0]\n\tActual  :{z_algo(word)}")

    word="bbabacacbacbaacacbbb"
    expected = [None, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 2, 1]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for bbabacacbacbaacacbbb!\n\tExpected:[None, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 2, 1]\n\tActual  :{z_algo(word)}")

    word="bbbbbccaccbbabb"
    expected = [None, 4, 3, 2, 1, 0, 0, 0, 0, 0, 2, 1, 0, 2, 1]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for bbbbbccaccbbabb!\n\tExpected:[None, 4, 3, 2, 1, 0, 0, 0, 0, 0, 2, 1, 0, 2, 1]\n\tActual  :{z_algo(word)}")

    word="accbbabacaabcbaaaccb"
    expected = [None, 0, 0, 0, 0, 1, 0, 2, 0, 1, 1, 0, 0, 0, 1, 1, 4, 0, 0, 0]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for accbbabacaabcbaaaccb!\n\tExpected:[None, 0, 0, 0, 0, 1, 0, 2, 0, 1, 1, 0, 0, 0, 1, 1, 4, 0, 0, 0]\n\tActual  :{z_algo(word)}")

    word="accaaabcacbacba"
    expected = [None, 0, 0, 1, 1, 1, 0, 0, 2, 0, 0, 2, 0, 0, 1]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for accaaabcacbacba!\n\tExpected:[None, 0, 0, 1, 1, 1, 0, 0, 2, 0, 0, 2, 0, 0, 1]\n\tActual  :{z_algo(word)}")

    word="bbacababcaaacbcbcbaa"
    expected = [None, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for bbacababcaaacbcbcbaa!\n\tExpected:[None, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]\n\tActual  :{z_algo(word)}")

    word="bcacabbacaaaaba"
    expected = [None, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for bcacabbacaaaaba!\n\tExpected:[None, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0]\n\tActual  :{z_algo(word)}")

    word="baaabaabbbbacccaabaa"
    expected = [None, 0, 0, 0, 3, 0, 0, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for baaabaabbbbacccaabaa!\n\tExpected:[None, 0, 0, 0, 3, 0, 0, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0]\n\tActual  :{z_algo(word)}")
        
    word="aabcaabxaaazabacaazaabccaabcaabxaaabaab"
    expected = [None, 1, 0, 0, 3, 1, 0, 0, 2, 2, 1, 0, 1, 0, 1, 0, 2, 1, 0, 4, 1, 0, 0, 0, 11, 1, 0, 0, 3, 1, 0, 0, 2, 3, 1, 0, 3, 1, 0]
    try:
        assert z_algo(word)[1:] == expected[1:]
    except AssertionError:
        print(f"Error computing Z-values for aabcaabxaaazabacaazaabccaabcaabxaaabaab!\n\tExpected:[None, 1, 0, 0, 3, 1, 0, 0, 2, 2, 1, 0, 1, 0, 1, 0, 2, 1, 0, 4, 1, 0, 0, 0, 11, 1, 0, 0, 3, 1, 0, 0, 2, 3, 1, 0, 3, 1, 0]\n\tActual  :{z_algo(word)}")


if __name__ == "__main__":
    test_z_alg()
