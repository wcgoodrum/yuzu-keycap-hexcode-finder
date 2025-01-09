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
		print("please enter a valid hex color code (like #0a1bc2)")
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
	print("keycap color not found, please choose a valid yuzu plastic name")
	exit()

if r == -1 and inputKeycap:
	print(colors[inputKeycap][3])
	exit()


numResults = 5
inputNumResults = input("number of results > ").strip()
print(inputNumResults)
if inputNumResults and inputNumResults.isdigit():
	numResults = int(inputNumResults)
	if numResults < 1 or numResults > 50:
		print("invalid choice for number of results, please choose a number 1-50")
		exit()


podium = []
testResult = ()
for key in colors:
	keyR = colors[key][0]
	keyG = colors[key][1]
	keyB = colors[key][2]
	rDist = (r - keyR) **2
	gDist = (g - keyG) **2
	bDist = (b - keyB) **2
	dist = rDist + gDist + bDist
	hexcode = colors[key][3]
	
	podium += [(key, hexcode, dist, keyR, keyG, keyB)]
    
	if inputKeycap and key == inputKeycap:
		testResult = (key, hexcode, dist, keyR, keyG, keyB)

podium.sort(key=lambda tup: tup[2])


def getColorLine(r, g, b, length):
	prefix = f"\033[48;2;{r};{g};{b}m"
	text = " "*length
	suffix = "\033[0m"
	return prefix+text+suffix


def getResultString(inputRgb, result):
	name = result[0].rjust(4)
	hexcode = result[1]
	dist = str(round(math.sqrt(result[2]), 4)).rjust(8)
	text = f"{name} ({hexcode}): {dist}"
	colorLine = getColorLine(result[3], result[4], result[5], 8)
	compareLine = getColorLine(inputRgb[0], inputRgb[1], inputRgb[2], 4)
	return text + (colorLine + compareLine)


print(f"nearest {numResults} keycap colors to #{inputHex}:")
for i in range(numResults):
	print(getResultString((r,g,b), podium[i]))

if testResult:
	print("test key result:")
	print(getResultString((r,g,b), testResult))
