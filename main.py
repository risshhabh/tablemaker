lines = open("input.txt", "r").read().splitlines()
out = open("output.txt", "w")

lines = [line.strip() for line in lines]

[out.write(line + "\n") if line[0] != "#" else ... for line in lines]



out.close()

print(f"Task finished.")