with open("sample_doc.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
file = open('New Document.txt', 'x')
import os
if os.path.exists("New Document.txt"):
    print("File exists!!!")
else:
    print("The file does not exist")

file = open("New Document.txt", "w")

import os
os.remove("sample_doc.txt")
import os
os.rmdir("sample folder")
file.close()