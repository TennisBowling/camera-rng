from PIL import Image
import subprocess
devNull = open('/dev/null', 'w')#used to output the fswebcam stdout and stderr
name = 0
while True:
    name = name + 1
    randomBits = ""
    pixelRow = 0
    pixelColumn = 0
    captureImage = subprocess.Popen(["fswebcam", "-r", "356x292", "-d", "/dev/video0", "static.jpg", "--skip", "10"], stdout=devNull, stderr=devNull) #assumes your camera is on /dev/video0
    captureImage.communicate()#executes the command detailed above with takes a picture using the webcam
    staticImage = Image.open("static.jpg")#Opens the image
    bW_Image = staticImage.convert('1')#Converts the image to a black or white image
    imageToProcess = bW_Image.load()#Saves the image to a variable that can be iterated through
    while pixelRow < staticImage.size[0]:#Iterates through the image pixel by pixel
        while pixelColumn < staticImage.size[1]:
            if imageToProcess[pixelRow, pixelColumn] == 0:
                randomBits = randomBits + "0"#Adds a 0 to the randomBits variable if the current pixel is white
            else:
                randomBits = randomBits + "1"#Adds a 1 to the randomBits variable if the current pixel is black
            pixelColumn = pixelColumn + 1
        pixelRow = pixelRow + 1
        pixelColumn = 0
    output = open('output.txt', 'w')
    output.write(str(int(randomBits, 2)))#Writes the randomBits Variable to the output file converted to a decimal number
    print int(randomBits, 2)#Also prints this decimal number to the terminal
    output.close()