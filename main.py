def rm_cmnts():
    lines = open("input.txt", "r").read().splitlines()
    lines = [line.strip() for line in lines]

    with open("output.txt", "w") as out:
        try:
            [out.write(line + "\n") if line[0] != "#" else ... for line in lines]
        except:
            raise

        out.close()
        return 0


print(f"Removed Comments with {rm_cmnts()}")
