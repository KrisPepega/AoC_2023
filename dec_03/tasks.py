file_str = open("input.txt", "r").read()

# file_str = file_str.replace(".", " ")


def check_adjacency(i):
    check_index = [1, -1, 141, -141, 140, -140, 142, -142]
    if i >= 141:
        if file_str[i + 141] is not "." and not (file_str[i + 141].isdigit()):
            pass
    return False


for i, c in enumerate(file_str):
    if c.isdigit():
        pass
    pass
