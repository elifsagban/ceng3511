import re
filename = "graph.txt"

# open the file for reading
filehandle = open(filename, 'r')
while True:
    # read a single line
    line = filehandle.readline()
    if not line:
        break
    result = re.findall(r'\d+', line)
    print(result)

# close the pointer to that file
filehandle.close()
