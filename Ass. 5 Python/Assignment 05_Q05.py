from cImage import *

def getnegativePixel(oldP):
    
    newGreen = (int(oldP.getGreen()/2))

    newRed = (int(oldP.getRed()/2))
    
    newBlue = (int(oldP.getBlue()/2))
    
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
            
            newP =  negativePixel(oldP)
            
            newImage.setPixel(col, row, newP)

    newImage.setPosition(w+1,0)
    
    newImage.draw(myImageWindow)
    
    myImageWindow.exitOnClick()

tomakenegative("pic.gif")
                

