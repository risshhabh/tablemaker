def init_files(filename: str = "input") -> list:
    try:
        lines = open(f"{filename}.txt", "r").read().splitlines()
    except FileNotFoundError:
        print("Looks like you don't have your files set up, I did it for you.")
        lines = open(f"{filename}.txt", "x").read().splitlines()
    
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