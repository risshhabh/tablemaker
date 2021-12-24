def init_files() -> list:
    try:
        print("Looks like you don't have your files set up, I did it for you.")
        return open("input.txt", "x").read().splitlines()
    except FileExistsError:
        return open("input.txt", "r").read().splitlines()


def rm_cmnts(lines: list) -> int:
    lines = [line.strip() for line in lines]

    with open("output.txt", "w") as out:
        try:
            [out.write(line + "\n") if line[0] != "#" else ... for line in lines]
        except:
            raise

        out.close()
        return 0


print(f"Removed Comments with {rm_cmnts()}")