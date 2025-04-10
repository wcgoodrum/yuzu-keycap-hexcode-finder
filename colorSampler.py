import os
import csv
import math
from PIL import Image

IMAGEDIR = "keyimages"
TOPLEFT = ( 63, 39)
BTMRGHT = (192, 80)

print("Slurping images from local path: " + IMAGEDIR)
totalPixs = (BTMRGHT[0] - TOPLEFT[0]) * (BTMRGHT[1] - TOPLEFT[1])
with open("colorvalues.csv", "w", newline='') as record:
    writer = csv.writer(record)
    writer.writerow(["yuzu name", "hex value", "red", "green", "blue"])
    
    fList = os.listdir(IMAGEDIR)
    for f in fList:
        print(f)
        image = Image.open(IMAGEDIR + "\\" + f, 'r').load()
        red = grn = blu = 0
        for x in range(TOPLEFT[0], BTMRGHT[0]):
            for y in range(TOPLEFT[1], BTMRGHT[1]):
                pixel = image[x, y]
                red += pixel[0]**2
                grn += pixel[1]**2
                blu += pixel[2]**2
                
        redAvr = round(math.sqrt(red/totalPixs))
        grnAvr = round(math.sqrt(grn/totalPixs))
        bluAvr = round(math.sqrt(blu/totalPixs))
        hexStr = '#' + hex(redAvr)[2:] + hex(grnAvr)[2:] + hex(bluAvr)[2:]
        writer.writerow([f.replace(".jpg",""), hexStr, str(redAvr), str(grnAvr), str(bluAvr)])
        
print("Done!")
