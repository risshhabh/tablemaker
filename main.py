def init_files(input_name: str = "input.txt", output_name: str = "output.txt") -> list:

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
    with open(filename) as file:
        lines = file.read().splitlines()
        [line.split("|").strip() for line in lines]

    return lines


splitted_lines = split_filelines("output.txt")

print("\n\n")
print()