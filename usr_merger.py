import sys
import os


input_folder_name = sys.argv[1]
output_file_name = sys.argv[2]

for filename in os.listdir(input_folder_name):
    wf = open(output_file_name, 'a', encoding="utf-8")
    wf.write("filename = "+filename+"\n")
    with open(os.path.join(input_folder_name, filename), 'r', encoding="utf-8") as file:
        read = file.read()
        file.seek(0)

        line = 1
        for word in read:
            if word == '\n':
                line += 1

        arr = []
        for i in range(line):
            arr.append(file.readline())

        for x in arr:
            wf.write(x)

    wf.write("\n")
