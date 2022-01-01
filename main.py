in_filename = r"raw.txt"
out_filename = r"out.txt"


# Initialize files.
try:
    lines = open(in_filename).read().splitlines()
except FileNotFoundError:
    print(
        f"Looks like you don't have your input file `{in_filename}` set up, I did it for you."
    )
    open(in_filename, "x")
    lines = open(in_filename).read().splitlines()

try:
    open(out_filename)
except FileNotFoundError:
    print(
        f"Looks like you don't have your output file `{out_filename}` set up, I did it for you."
    )
    open(out_filename, "x")

if len(lines) == 0:
    exit()


# Remove comments and newlines
lines = [line.strip() for line in lines]

with open(out_filename, "w") as out:
    [
        ((out.write(f"{line}\n") if line[0] != "#" else ...) if len(lines) > 0 else ...)
        for line in lines
    ]


# Split file-lines by pipe characters ("|")
# Output is 2D list.

with open(out_filename) as file:
    splitted_lines = [
        [inner.strip() for inner in line]  # Then strip whitespaces.
        # First split each line in file.
        for line in [line.split("|") for line in file.read().splitlines()]
    ]


# Convert to columns
from itertools import zip_longest


"""
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

columnized = list(zip_longest(*splitted_lines, ""))
# Nifty trick; `fillvalue` parameter replaces `None`s with `""` rather than leaving it empty.

# Find the length of the padding for each column.

padding = [(max(len_col) + 2) for len_col in [[map(len, col)] for col in columnized]]


# Pad elements.

for col in range(len((padded := columnized.copy()))):
    padded[col] = [el.center(padding[col]) for el in padded[col]]


# Convert columns to rows.
tbar = f"┌{'┬'.join(['─' * pad for pad in padding])}┐\n"
mbar = f"├{'┼'.join(['─' * pad for pad in padding])}┤\n"
bbar = f"└{'┴'.join(['─' * pad for pad in padding])}┘\n"

out_to_file: list[str] = []

for row in range(len(padded[0])):
    out_to_file.append("│" + "│".join([col[row] for col in padded]) + "│")

with open(out_filename, "w") as file:
    while True:

        # Made permanently "no"
        choice = "n"  # input("Want bars in between lines? [Y/N]\n--> ")
        if choice in ("y", "n", "yes", "no"):
            break
        print("Invalid input; try again.")

    file.write(tbar)

    # Without middle bars, just make `mbar` empty string.
    if choice in ("n", "no"):
        mbar = ""

    for line in out_to_file[:-1]:
        file.writelnies((line, "\n", mbar))
    file.write(out_to_file[-1] + f"\n{bbar}")
