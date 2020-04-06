import csv

with open('numbers.txt', mode='r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		numbers=row

numCounts=[]

for num in numbers:
	numCounts.append( [num, numbers.count(num)] )

numCounts=list(set(map(tuple, numCounts)))
numCounts.sort(key=lambda elem: elem[1])

with open('sorted.txt', mode='w') as sorted_file:
	writer=csv.writer(sorted_file, delimiter=',')
	for tups in numCounts[::-1]:
		writer.writerow(tups)