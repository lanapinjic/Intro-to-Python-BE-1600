from cImage import *

def getnegativePixel(oldP):
    
    newGreen = (int(oldP.getGreen()/128))*255

    newRed = (int(oldP.getRed()/128))*255
    
    newBlue = (int(oldP.getBlue()/128))*255
    
    newP = Pixel(newRed, newGreen, newBlue)
    
    return newP



def tomakenegative(imageFile):
    
    oldImage = FileImage(imageFile)
    
    w = oldImage.getWidth()
    
    h = oldImage.getHeight()

    myImageWindow = ImageWin("Negative Image", w *2, h)
    
    oldImage. draw(myImageWindow)
    
    newIm = EmptyImage(w,h)

    for row in range(h):
        for col in range(w):
            oldP = oldImage.getPixel(col, row)
            
            newP = (oldP.getred() + oldP.getGreen() + oldP.getBlue())/3
            #how to distinguish what to change 
            if newP < 128:
                newPtwo = Pixel(0,0,0)
            else:
                newPtwo = Pixel(255,255,255)
                
            newP = negativePixel(oldP)
            
            newImage.setPixel(col, row, newPtwo)

    newImage.setPosition(w+1,0)
    
    newImage.draw(myImageWindow)
    
    myImageWindow.exitOnClick()

tomakenegative("Butterfly.gif")
                
