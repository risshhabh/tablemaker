def init_files(filename: str = "table.txt") -> list:
    """
    Initializes the file if not already.
    `filename` is going to be the input, converted to output in end.
    """

    try:
        lines = open(filename).read().splitlines()
    except FileNotFoundError:
        print("Looks like you don't have your table file set up, I did it for you.")
        open(filename, "x")
        lines = open(filename).read().splitlines()

    return lines


lines = init_files("table.txt")


def rm_cmnts(lines: list, filename: str = "table.txt"):
    """
    Removes the comments in the table file.
    `lines` is just the lines of the file.
    Using `lines`, remove comments in `table.txt`.
    """
    lines = [line.strip() for line in lines]

    with open(filename, "w") as out:
        [out.write(line + "\n") if line[0] != "#" else ... for line in lines]


rm_cmnts(lines, "table.txt")
print(f"Removed Comments in table file.")


def split_filelines(filename: str = "table.txt") -> list[list]:
    """
    Splits lines with "|" and returns nested list.
    `filename` is just the input without comments.
    Output is a list nested with each element being a table row.
    """
    with open(filename) as file:
        lines = [
            [inner.strip() for inner in line]  # Second strip whitespaces
            # First split each line in file.
            for line in [line.split("|") for line in file.read().splitlines()]
        ]

    return lines


splitted_lines = split_filelines("output.txt")
print("Splitted lines into lists.")


def padding_len(nested: list) -> int:
    """
    Returns the length of the longest element in the table.
    `nested` is simply a 2D list of the table elements.
    """

    # First make a list of the lengths of each separate table element.
    lens: list[list[int]] = [[map(len, el) for el in nest] for nest in nested]

    # Make list of longest lengths in each nested list.
    maxes: list[int] = [max(nest) for nest in lens]

    # Finally get longest length. Add 2 for more padding.
    return [max(el) for el in maxes][0] + 2


padding = padding_len(splitted_lines)
print("Found padding value.")


def pad_elements(unpadded: list) -> list[list]:
    """
    Pads and centers the elements inside of the list.
    `unpadded` is simply the 2D list of elements.
    Output is a padded version of the Nested List.
    """

    return [[el.center(padding) for el in row] for row in unpadded]


padded = pad_elements(splitted_lines)
print("Padded list.")
