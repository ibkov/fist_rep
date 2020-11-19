f = open("l2.txt")
map = [[k for k in i] for i in f.read()[:-4].split("\n")]
map[1][1] = "\u00B7"
map[1][2] = "\u00B7"
map[1][3] = "\u00B7"
map[0][3] = "\u00B7"
red = "\033[34m"
white = "\033[31m"
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "\u00B7":
            print(red + map[i][j], end='\t')
        else:
            print(white + map[i][j], end='\t')
    print()

