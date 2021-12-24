def init_files(input_name: str = "input.txt", output_name: str = "output.txt") -> list:
    
    # Input
    try:
        lines = open(f"{input_name}", "r").read().splitlines()
    except FileNotFoundError:
        print("Looks like you don't have your files set up, I did it for you.")
        open(f"{input_name}", "x")
        lines = open(f"{input_name}", "r").read().splitlines()

    # Output
    try:
        open(f"{output_name}", "r")
    except FileNotFoundError:
        open(f"{output_name}", "x")

    return lines


lines = init_files()


def rm_cmnts(lines: list) -> int:
    lines = [line.strip() for line in lines]

    with open("output.txt", "w") as out:
        try:
            [out.write(line + "\n") if line[0] != "#" else ... for line in lines]
        except:
            raise

        out.close()
        return 0


print(f"Removed Comments with {rm_cmnts(lines)}")
