from cImage import *

#user input
global x,y
x = int(input("enter x deminsion: "))
y = int(input("enter y deminsion: "))

#function to get old image dimestions and convert
def dimesn(oldImage):
    oldWidth = oldImage.getWidth()
    
    oldHeight = oldImage.getHeight()
    
    global x,y
    
    newImage = EmptyImage(oldWidth * x, oldHeight *y)
    
    for row in range(newImage.getHeight()):
        for col in range(newImage.getWidth()):
            ogCol = col //x
            
            ogRow = row//y
            
            oldPixel = oldImage,getPixel(ogCol, ogRow)
            

            newImage.setPixel(col, row, oldPixel)

    return newImage
#function to make the new image from the information and change the height and width
def makingnewImage(imageFile):
    
    oldImage = FileImage(imageFile)
    
    w = oldImage.getWidth()
    
    h = oldImage.getHeight()

    myWin = ImageWin("New Image", w * x, h * y)
    
    newImage = dimesn(oldImage)
    
    newImage.draw(myWin)
    
    myWin.exitOnClick ()

makingnewImage("butterfly.gif")
    
