def init_files(input_name: str = "input.txt", output_name: str = "output.txt") -> list:
    """Initializes the files if not already."""

    # Input
    try:
        lines = open(input_name).read().splitlines()
    except FileNotFoundError:
        print("Looks like you don't have your files set up, I did it for you.")
        open(input_name, "x")
        lines = open(input_name).read().splitlines()

    # Output
    try:
        open(output_name)
    except FileNotFoundError:
        open(output_name, "x")

    return lines


lines = init_files("input.txt", "output.txt")


def rm_cmnts(lines: list, output_name: str = "output.txt") -> int:
    """Removes the comments in the input file, outputs in output file."""
    lines = [line.strip() for line in lines]
    err = 0

    with open(output_name, "w") as out:
        try:
            [out.write(line + "\n") if line[0] != "#" else ... for line in lines]
        except:
            err += 1

        out.close()
        return err


print(f"Removed Comments with {rm_cmnts(lines, 'output.txt')}")


def split_filelines(filename: str = "output.txt") -> list[list]:
    """Splits lines with "|" and returns nested list."""
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
    """Returns the length of the longest element in the table."""

    # First make a list of the lengths of each separate table element.
    lens: list[list[int]] = [[map(len, el) for el in nest] for nest in nested]
    
    # Make list of longest lengths in each nested list.
    maxes: list[int] = [max(nest) for nest in lens]
    
    # Finally get longest length.
    return [max(el) for el in maxes][0]