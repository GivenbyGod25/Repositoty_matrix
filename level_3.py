data = []
datawork = []
with open('file_for_level_3.txt', 'r') as file:
    for line in file:
        s = line.split()
        data.append( [ int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]) ] )
        datawork.append([int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4])])

for i in range(5):
    for j in range(5):
        datawork[i][j] = ((data[i][j] ** 2 - 6) * 3)

k = 0
for i in range(5):
    for j in range(5):
        if len(str(data[i][j])) == 2:
            if abs((data[i][j] // 10) - (data[i][j] % 10)) == 1:
                k += 1
mas = []
for i in range(5):
    for j in range(5):
        if datawork[i][j] % k == 0:
            mas.append(datawork[i][j])
maxs = 0
for i in range(len(mas)):
    s = 0
    x = str(mas[i])
    for j in range(len(x)):
        s += int(x[j])
    if s > maxs:
        maxs = s
print(maxs)