def elias_omega_encode(n: int) -> str:
    bin_n_min = bin(n)[2:]
    # print(bin_n_min)
    encoded_string = str(bin_n_min)
    # print(f"encoded_string: {encoded_string}")
    length = len(bin_n_min)
    # print(length)
    length_component = length
    # once the length of the Ln == 1, STOP encoding
    while length_component != 1:
        length_component =  length_component - 1
        # print(f"length_component={length_component}")

        bn_lc = bin(length_component)[2:]
        # print(f"bn_lc={bn_lc}")

        # change leading 1 to 0
        bn_lc_encode = str(0) + bn_lc[1:]
        # print(f"bn_lc_after={bn_lc_encode}")

        # add to encoded string
        encoded_string = bn_lc_encode + encoded_string
        # print(f"encoded_string={encoded_string}")

        # update length_component
        length_component = len(bn_lc_encode)
        # print()

    return encoded_string



if __name__ == '__main__':
    n = 561
    encoded_n = elias_omega_encode(n)
    print(f"encoded_n={encoded_n}")
