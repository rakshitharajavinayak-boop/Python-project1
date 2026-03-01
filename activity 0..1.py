with open(r"C:\Users\rajav\OneDrive\Desktop\Rakshitha\Repeated.txt", "r") as inputFile, \
open(r"C:\Users\rajav\OneDrive\Desktop\Rakshitha\UpdatedFile.txt", "w") as outputFile:
lines_seen_so_far = set()

for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)
        print("Done")