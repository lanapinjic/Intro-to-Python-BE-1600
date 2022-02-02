from cImage import *

def redInt(oldPixel):
    oldGreen = oldPixel.getGreen()
    
    oldBlue = oldPixel.getBlue()
    
    if oldPixel.getRed() < 200:
        newRed = oldPixel.getRed() + 100
    else:
        newRed = oldPixel.getRed()
        
    newPixel = Pixel(newRed, oldGreen, oldBlue)
    
    return newPixel



def makeitRed(imageFile):
    oldImage = FileImage(imageFile)
    
    width = oldImage.getWidth()
    
    height = oldImage.getHeight()

    myImageWindow = ImageWin("New Image", width * 2, height)
    
    oldImage.draw(myImageWindow)
    
    newImage = EmptyImage(width,height)

    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col,row)
            
            newPixel = redInt(oldPixel)
            
            newIm.setPixel(col,row,newPixel)

    newImage.setPosition(width +1,0)
    
    newImage.draw(myImageWindow)
    
    myImageWindow.exitOnClick()
            
makeitRed("butterfly.gif")


