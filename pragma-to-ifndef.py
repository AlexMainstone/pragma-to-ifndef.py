import os
print("Enter the path to your .h files")
path = input(":>")

for file in os.listdir(path):
    if file.endswith(".h") or file.endswith(".hpp"):
        deftitle = file
        deftitle = deftitle.replace(".", "_") + "_"
        deftitle = deftitle.upper()

        # remove "#pragma once" and add the ifndef
        with open(path + "/" + file, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(path + "/" + file, 'w') as fout:
            fout.writelines(["#ifndef " + deftitle + "\n" + "#define " + deftitle + "\n"] + data[1:] + ["\n#endif // " + deftitle])
        
        print(file + " > " + deftitle)
