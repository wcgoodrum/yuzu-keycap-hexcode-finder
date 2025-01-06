import csv
import math


inputHex = input("hexcode to search > ").strip().strip('#').lower()
r = g = b = -1
if inputHex:
	try:
		if len(inputHex) != 6: raise ValueError()
		r = int(inputHex[0:2], 16)
		g = int(inputHex[2:4], 16)
		b = int(inputHex[4:6], 16)
	except ValueError:
		print("please enter a valid hex color code")
		exit()
		

inputKeycap = input("key color to test > ").strip().lower()
colors = {}
path = "colorvalues.csv"
with open(path, 'r') as f:
	csvFile = csv.reader(f)
	for line in csvFile:
		if line[0] != "yuzu name":
			colors[line[0]] = (int(line[2]), int(line[3]), int(line[4]), line[1])

if inputKeycap and inputKeycap not in colors:
	print("keycap color not found")
	exit()

if r == -1 and inputKeycap:
	print(colors[inputKeycap][3])
	exit()


numResults = 3
inputNumResults = input("number of results (1-20) > ").strip()
print(inputNumResults)
if inputNumResults and inputNumResults.isdigit():
    numResults = int(inputNumResults)
    if numResults < 1 or numResults > 20:
        print("invalid choice for number of results")
        exit()
	

podium = []
testResult = ()
for key in colors:
	rDist = (r - colors[key][0]) **2
	gDist = (g - colors[key][1]) **2
	bDist = (b - colors[key][2]) **2
	dist = rDist + gDist + bDist
	hexcode = colors[key][3]
	
	podium += [(key, hexcode, dist)]
    
	if inputKeycap and key == inputKeycap:
	    testResult = (key, hexcode, dist)

podium.sort(key=lambda tup: tup[2])


print(f"nearest {numResults} keycap colors to #{inputHex}:")
for i in range(numResults):
	name = podium[i][0].rjust(4)
	hexcode = podium[i][1]
	dist = str(math.sqrt(podium[i][2]))
	print(f"{name} ({hexcode}): {dist}")

if testResult:
	print("test key result:")
	name = testResult[0].rjust(4)
	hexcode = testResult[1]
	dist = str(math.sqrt(testResult[2]))
	print(f"{name} ({hexcode}): {dist}")
