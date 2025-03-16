import csv
import math


def getColorDictionary(path: str) -> dict:		
	colors = {}
	with open(path, 'r') as f:
		csvFile = csv.reader(f)
		for line in csvFile:
			if line[0] != "yuzu name":
				colors[line[0]] = (int(line[2]), int(line[3]), int(line[4]), line[1])
	return colors

def hexToRGB(hexcode: str) -> tuple:
    hexcode = hexcode.lower().strip().strip('#')
    try:
        if len(hexcode) != 6: raise ValueError()
        r = int(hexcode[0:2], 16)
        g = int(hexcode[2:4], 16)
        b = int(hexcode[4:6], 16)
        return (r,g,b)
    except ValueError:
        return (-1,-1,-1)
    
def getDistancesFromColor(rgb: tuple, colors: dict) -> list:
	podium = []
	for key in colors:
		r = rgb[0]
		g = rgb[1]
		b = rgb[2]
		keyR = colors[key][0]
		keyG = colors[key][1]
		keyB = colors[key][2]
		rDist = (r - keyR) **2
		gDist = (g - keyG) **2
		bDist = (b - keyB) **2
		dist = rDist + gDist + bDist
		hexcode = colors[key][3]

		podium += [(key, hexcode, dist, keyR, keyG, keyB)]
	
	podium.sort(key=lambda tup: tup[2])
	return podium
 
def getColorBlockLine(rgb: tuple, length: int) -> str:
	r = rgb[0]
	g = rgb[1]
	b = rgb[2]
	prefix = f"\033[48;2;{r};{g};{b}m"
	text = " "*length
	suffix = "\033[0m"
	return prefix+text+suffix

def getResultString(inputRgb: tuple, result: tuple) -> str:
	name = result[0].rjust(4)
	hexcode = result[1]
	dist = str(round(math.sqrt(result[2]), 4)).rjust(8)
	text = f"{name} ({hexcode}): {dist}"
	colorLine = getColorBlockLine((result[3], result[4], result[5]), 8)
	compareLine = getColorBlockLine(inputRgb, 4)
	return text + (colorLine + compareLine)


def main():
	path = "colorvalues.csv"
	colors = getColorDictionary(path)
	if not colors: 
		print("Couldn't find any colors in path given (check path and file).");exit()

	inputHex = input("Hexcode to search > ")
	rgb = hexToRGB(inputHex)
	if inputHex != "" and rgb == (-1,-1,-1):
		print("Invalid color hexcode entered.");exit()

	inputKeycap = input("Key color to test > ").strip().lower()
	if inputKeycap != "" and inputKeycap not in colors:
		print("Invalid Yuzu keycap color name entered.");exit()

	if rgb == (-1,-1,-1) and inputKeycap:
		print(colors[inputKeycap][3]);exit()

	numResults = 5
	inputNumResults = input("Number of results > ").strip()
	if inputNumResults and inputNumResults.isdigit():
		numResults = int(inputNumResults)
	if numResults < 1 or numResults > 50:
		print("Invalid choice for number of results. Please choose a number 1-50.");exit()

	podium = getDistancesFromColor(rgb, colors)
	print(f"nearest {numResults} keycap colors to #{inputHex}:")
	for i in range(numResults):
		print(getResultString(rgb, podium[i]))

	if inputKeycap:
		testResult = getDistancesFromColor(rgb, {inputKeycap: colors[inputKeycap]})[0]
		print("test key result:")
		print(getResultString(rgb, testResult))
    
if __name__ == "__main__":
    main()
    
