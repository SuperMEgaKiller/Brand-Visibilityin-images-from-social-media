'''
Tool for work with a Image
All images should be the same size

'''
from PIL import Image
import numpy as np


class ImageProcessing(object):
    """

    """
    Wight = 720
    Height = 720
    imgLen = Wight * Height
    RGB = 3
    inputLen = imgLen * RGB

    def __init__(self, *args):  # as INPUT take a list of Images Names
        """
        :param args: # list of Images Names
        """
        self.listOfImages = list()
        for picture in args:
            if not self.Valid(picture):
                self.resizeImage(picture)
            self.listOfImages.append(picture)

    def addImages(self, *args):
        """
        :type args: Tuple
        :param args: # list of Images Names
        :return: None
        """
        for picture in args:
            if not self.Valid(picture):
                self.resizeImage(picture)
            self.listOfImages.append(picture)

    def showHead(self):
        """
        Show 5 head Images from List,
        if List size less than 5 show all Images
        :return: None
        """
        assert (len(self.listOfImages) != 0), "Theres no Images to show"
        tmp = 5  # number of images to show
        if len(self.listOfImages) < tmp:  # check is number of Images is less than 5
            tmp = len(self.listOfImages)

        for index in range(tmp):  # show top 5 Images
            tmpImage = Image.open(self.listOfImages[index], 'r')
            tmpImage.show()

    def Valid(self, name: str) -> bool: # tutaj poprostu podajemy jakiego typu oczekujemy wartosc 'name' 
        #i co zwraca ta funkcja czyli True or False
        
        assert (isinstance(name, str) and name.endswith('.jpg')), ' Invalid Input Argument'
        tmpPicture = Image.open(name, 'r')
        w, h = tmpPicture.size

        return w * h == ImageProcessing.imgLen  # True if size of read Image is equal to expected

    def resizeImage(self, name: str) -> None:
        openImg = Image.open(name, 'r')
        print('Image old sie {} {}'.format(name, openImg.size))
        newImg = openImg.resize((ImageProcessing.Wight, ImageProcessing.Height))
        #newImg.save(str(ImageProcessing.Wight) + 'x' + str(ImageProcessing.Height) + name)
        print('Image new sie {} {}'.format(name, newImg.size))
        newImg.save(name)

    def getRGBMatrix(self):
        """
        creates Matrix (number of pictures, Wight * Height * 3) 
        :return: self.RGBMatrix - RGB matrix of all pixels for every Image 
        """

        self.RGBMatrix = np.empty((0, ImageProcessing.inputLen), dtype=np.int32)  # Matrix of pixels values for every picture

        for picture in self.listOfImages:
            tmpPicture = Image.open(picture, 'r')  # Open the Image
            R, G, B = tmpPicture.split()
            r = np.reshape(R,(1, ImageProcessing.imgLen)); g = np.reshape(G,(1, ImageProcessing.imgLen)); b = np.reshape(B,(1, ImageProcessing.imgLen))
            rgb = np.concatenate((r, g, b), axis=1)
            #Colour = np.reshape(Colour, (len(self.listOfImages), self.lenOfPixels))
            self.RGBMatrix = np.append(self.RGBMatrix, rgb, axis=0)
            
        return self.RGBMatrix  # return Matrix of pixels



if __name__ == '__main__':
    New = ImageProcessing('godzilla.jpg', 'nike2.jpg')
    New.showHead()
