def get_z_value(str, i):
    z_value = 0
    compare_index = 0
    while i<len(str) and compare_index<len(str) and str[i] == str[compare_index] :
        z_value += 1
        compare_index +=1 
        i += 1
    return z_value

def get_rk(str,i):
    if i < 1 or i>=len(str): 
        print("Error")
    z_value = get_z_value(str, i)
    if z_value == 0: 
        return get_rk(str, i-1)


def z_algo(string):
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
        print("i_value", i, "letter", string[i])
        if i > r_arr[i-1]: # Case 1 
            print("Case 1")
            z_value = 0
            compare_index = 0 # starting index from first character in the string
            k=i
            while k<len(str) and compare_index<len(str) and str[k] == str[compare_index]:
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
                print("Case 2a", z_arr[i-l_arr[i-1]+1],  r_arr[i-1]-i+1)
                z_value = z_arr[i-l_arr[i-1]+1-1] # removed the + 1 is this correct
                l_value = l_arr[i-1]
                r_value = r_arr[i-1]

            else: 
                print("Case 2b")
                z_value = 0
                compare_index = 0
                k=i
                while k<len(str) and compare_index<len(str) and str[k] == str[compare_index] :
                    z_value += 1
                    compare_index +=1 
                    k += 1
                r_value = k-1
                l_value = i
        print("z_value", z_value, "r_value", r_value, "l_value", l_value)
        print()
                

        z_arr[i] = z_value
        l_arr[i] = l_value
        r_arr[i] = r_value


    return z_arr, r_arr, l_arr
    


def z_gusfield(str, pat, arr): 
    pass


if __name__ == "__main__": 
    str = "cbbcaaccccbbccb"
    print(z_algo(str))

    







