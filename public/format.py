import csv
import ast
import json

f = open('electiontweets_hillary.csv')
csv_f = csv.reader(f)

data = []
for row in csv_f:
    for coordstr in row:
        coordnum = ast.literal_eval(coordstr)
        data.append(coordnum[0])
        data.append(coordnum[1])
        data.append(10)
        data.append(0)

f2 = open('electiontweets_trump.csv')
csv_f2 = csv.reader(f2)

for row in csv_f2:
    for coordstr in row:
        coordnum = ast.literal_eval(coordstr)
        data.append(coordnum[0])
        data.append(coordnum[1])
        data.append(10)
        data.append(1)


with open('data.json', 'wb') as outfile:
    json.dump(data, outfile)
