

def string_to_binary(bin_repr: str) -> bin:
    bin_result = 0
    for msb in bin_repr:
        bin_result = (bin_result << 1) | (1 if msb == "1" else 0)
    return bin(bin_result)


print(string_to_binary("101"))
