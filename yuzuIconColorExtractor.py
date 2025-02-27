import os
import csv
import math
from PIL import Image

# relative path to look in
path = "keyimages"
# square to sample from
uprLftCorner = [ 63, 39]
lwrRgtCorner = [192, 80]

bgnX = uprLftCorner[0]
endX = lwrRgtCorner[0]
bgnY = uprLftCorner[1]
endY = lwrRgtCorner[1]
totalPixs = (endX-bgnX) * (endY-bgnY)

record = open("colorvalues.csv", "wb")
fList = os.listdir(path)
with open("colorvalues.csv", "w", newline='') as record:
    writer = csv.writer(record)
    writer.writerow(["yuzu name", "hex value", "red", "green", "blue"])
    
    for f in fList:
        print(f)
        image = Image.open(path + "\\" + f, 'r').load()
        red = grn = blu = 0
        for i in range(bgnX, endX):
            for j in range(bgnY, endY):
                pixel = image[i,j]
                red += pixel[0]**2
                grn += pixel[1]**2
                blu += pixel[2]**2
                
        redAvr = round(math.sqrt(red/totalPixs))
        grnAvr = round(math.sqrt(grn/totalPixs))
        bluAvr = round(math.sqrt(blu/totalPixs))
        hexStr = '#' + hex(redAvr)[2:] + hex(grnAvr)[2:] + hex(bluAvr)[2:]
        writer.writerow([f.replace(".jpg",""), hexStr, str(redAvr), str(grnAvr), str(bluAvr)])
        
print("done!")
