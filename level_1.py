data = []
with open('file_for_level_1.txt', 'r') as file:
    for line in file:
        s = line.split()
        data.append( [ int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]) ] )

datamain = []
for i in range(5):
    for j in range(5):
        if i == j:
            datamain.append(data[i][j])
m = max(datamain)
for i1 in range(5):
    for j1 in range(5):
        x1 = data[i1][j1]
        for i2 in range(5):
            for j2 in range(5):
                x2 = data[i2][j2]
                p = x1 * x2
                if p == m:
                    print(x1+x2)
                    exit()