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


def split_filelines(filename: str = global_filename) -> list[list]:
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
print("Splitted lines into lists.")


from itertools import zip_longest


def convert_to_col(splitted: list[list[str]]):
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
print("Columnized the 2D list.")


def padding_len(col_list: list[list[str]]) -> list[int]:
    """
    Returns the length of the longest element in each column in the table.
    `col_list` is simply a 2D list of the columns in the table.
    """

    return map(max, [map(len, col) for col in col_list])


padding = padding_len(columnized)
print("Found padding values.")


def pad_elements(col_list: list[list[str]]) -> list[list]:
    """
    Pads and centers the elements inside of the list.
    `col_list` is simply the 2D list of elements, in columns.
    Output is a padded version of the Nested List.
    """

    for row in col_list:

        for ind in range(len(row)):
            ...


padded = pad_elements(splitted_lines)
print("Padded list.")
