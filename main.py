global_filename: str = "table.txt"  # Name of input (and output) file.


def init_files(filename: str = global_filename) -> list:
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


lines = init_files(global_filename)
exit() if len(lines) == 0 else ...

def rm_cmnts(lines: list, filename: str = global_filename):
    """
    Removes the comments in the table file.
    `lines` is just the lines of the file.
    Using `lines`, remove comments in `table.txt`.
    """
    lines = [line.strip() for line in lines]

    with open(filename, "w") as out:
        [out.write(line + "\n") if line[0] != "#" else ... for line in lines]


rm_cmnts(lines, global_filename)
print(f"Removed Comments in table file.")


def split_filelines(filename: str = global_filename) -> list[list[str]]:
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


splitted_lines = split_filelines(global_filename)
print(f"Splitted lines into lists: \n{splitted_lines}")


from itertools import zip_longest


def convert_to_col(splitted: list[list[str]]) -> list[list[str, None]]:
    """
    Essentially makes a list of columns rather than rows.

    Example:

    [
        [10, 11, 12],
        [13, 14, 15, 16],
        [17, 18, 19],
        [20, 21]
    ]

    Becomes:

    [
        (10,   13,   17,   20),
        (11,   14,   18,   21),
        (13,   15,   19, None),
        (16, None, None, None)
    ]
    """

    return list(zip_longest(*splitted))


columnized = convert_to_col(splitted_lines)
print(f"Columnized the 2D list: \n{columnized}")


def remove_Nones(None_col_list: list[list[str, None]]) -> list[list[str]]:
    """Removes the padding `None`s from the 2D list that are created by itertools.zip_longest()"""

    return [
        [(el if el is not None else "") for el in nested] for nested in None_col_list
    ]


columnized = remove_Nones(columnized)
print(f"Removed `None`s from columnized list: \n{columnized}")


def padding_len(col_list: list[list[str]]) -> list[int]:
    """
    Returns the length of the longest element in each column in the table.
    `col_list` is simply a 2D list of the columns in the table.
    """

    return [
        (max(len_col) + 2) for len_col in [[len(el) for el in col] for col in col_list]
    ]


padding = padding_len(columnized)
print(f"Found padding values: \n{padding}")


def pad_elements(col_list: list[list[str]], padding: list[int]) -> list[list[str]]:
    """
    Pads and centers the elements inside of the list.
    `col_list` is simply the 2D list of elements, in columns.
    Output is a padded version of the Nested List.
    """

    out = col_list.copy()

    for col in range(len(out)):
        out[col] = [el.center(padding[col]) for el in out[col]]

    return out


padded = pad_elements(columnized, padding)
print(f"Padded list: \n{padded}")

def convert_to_row(padded_cols):
    """Converts `padded_cols` (2D list of padded columns) back to row"""
    

# Not working as intended.
def write_out(padded_col_list: list[list[str]], padding: list[int]):
    """Finally writes the output into the `global_filename` file."""
    bar = "+" + "+".join(["-" * pad for pad in padding]) + "+\n"
    out_to_file: list[str] = []

    for row in range(len(padded_col_list[0])):
        out_to_file.append("|" + "|".join([col[row] for col in padded_col_list]) + "|")

    with open(global_filename, "w") as file:
        for line in out_to_file:
            file.writelines([bar, line, "\n"])
        file.writelines([bar, "\n"])


write_out(padded, padding)
print(f"Wrote to {global_filename}: \n{padded}")