data = []
with open('file_for_level_2.txt', 'r') as file:
    for line in file:
        s = line.split()
        data.append( [ int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]) ] )

for i in range(5):
    for j in range(5):
        data[i][j] = ((data[i][j] * 4 - 6) * 10 + ((data[i][j] // 13) * 7))

for i in range(5):
    for j in range(5):
        if (data[i][j] ** 0.5) % 1 == 0 and len(str(data[i][j])) == 4:
            x1 = int( str(data[i][j])[0] + str(data[i][j])[1])
            d = 2
            while d*d <= x1:
                if x1 % d == 0:
                    mind1 = d
                    break
                d += 1
            x2 = int(str(data[i][j])[2] + str(data[i][j])[3])
            d = 2
            while d * d <= x2:
                if x1 % d == 0:
                    mind2 = d
                    break
                d += 1

            if mind1 == mind2:
                print(data[i][j])
                exit()