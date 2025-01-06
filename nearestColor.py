import csv
import math

inputHex = input("hexcode to search > ").strip().strip('#').lower()
inputKeycap = input("key color to test > ").strip().lower()

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


colors = {}
path = "colorvalues.csv"
with open(path, 'r') as f:
	csvFile = csv.reader(f)
	for line in csvFile:
		if line[0] != "yuzu name":
			colors[line[0]] = (int(line[2]), int(line[3]), int(line[4]), line[1])

if inputKeycap and inputKeycap not in colors:
	print("keycap color not found")
	testKeycap = ""

if r == -1 and inputKeycap:
	print(colors[inputKeycap][3])
	exit()


podium = [("xxxx", float('inf'), "xxxxxx")] * 3
for key in colors:
	rDist = (r - colors[key][0]) **2
	gDist = (g - colors[key][1]) **2
	bDist = (b - colors[key][2]) **2
	dist = rDist + gDist + bDist
	hexcode = colors[key][3]
	
	if dist < podium[0][1]:
		podium[2] = podium[1]
		podium[1] = podium[0]
		podium[0] = (key, dist, hexcode)
	elif dist < podium[1][1]:
		podium[2] = podium[1]
		podium[1] = (key, dist, hexcode)
	elif dist < podium[2][1]:
		podium[2] = (key, dist, hexcode)

	if inputKeycap and key == inputKeycap:
		podium += [(key, dist, hexcode)]
		
print(f"nearest 3 keycap colors to #{inputHex}:")
for result in podium:
	name = result[0].rjust(4)
	hexcode = result[2]
	dist = str(math.sqrt(result[1]))
	print(f"{name} ({hexcode}): {dist}")
