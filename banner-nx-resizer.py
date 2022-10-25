from PIL import Image
import os
inputfiles=os.listdir("input")
for inputfile in inputfiles:
    asset=Image.open("input/" + inputfile)
    result=asset.resize((1024,512))
    result.save("output/" + inputfile.split(".")[0] + ".png")
