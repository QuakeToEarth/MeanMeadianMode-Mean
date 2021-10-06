import csv
f = open("data.csv")
reader = csv.reader(f)
data = list(reader)
sum = 0
for i in range(1, len(data)):
    c = (float(data[i][1]))
    sum = sum+c
mean = sum/len(data)
print(mean)