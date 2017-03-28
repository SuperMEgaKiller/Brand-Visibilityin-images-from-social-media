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

    def __init__(self, *args):  # as INPUT take a list of Images Names
        """
        :param args: # list of Images Names
        """
        self.lenOfPixels = ImageProcessing.Wight * ImageProcessing.Height
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
            if self.Valid(picture):
                self.listOfImages.append(picture.strip())

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

    def Valid(self, name: str) -> bool:
        assert (isinstance(name, str) and name.endswith('.jpg')), ' Invalid Input Argument'
        tmpPicture = Image.open(name, 'r')
        w, h = tmpPicture.size

        return w * h == self.lenOfPixels  # True if size of read Image is equal to expected

    def resizeImage(self, name: str) -> None:
        openImg = Image.open(name, 'r')
        print('Image old sie {} {}'.format(name, openImg.size))
        newImg = openImg.resize((ImageProcessing.Wight, ImageProcessing.Height))
        #newImg.save(str(ImageProcessing.Wight) + 'x' + str(ImageProcessing.Height) + name)
        print('Image new sie {} {}'.format(name, newImg.size))
        newImg.save(name)

    def getRGBColour(self, color = 'red'):
        """
        creates Matrix (number of pictures, 989 * 989) of one RGB Colour
        :return: self.ColourMatrix - matrix of RGB pixels values for every Image
        """
        self.numOfImages = len(self.listOfImages)  # Nr of images
        self.ColourMatrix = np.empty((0, self.lenOfPixels), dtype=np.uint8)  # Matrix of pixels values for every picture

        for picture in self.listOfImages:
            tmpPicture = Image.open(picture, 'r')  # Open the Image
            R, G, B = tmpPicture.split()

            Colour = np.array({
                'red': R,
                'green': G,
                'blue': B
            }.get(color, 'Wrong Color'))
            Colour = np.reshape(Colour, (len(self.listOfImages), self.lenOfPixels))
            self.ColourMatrix = np.append(self.ColourMatrix, Colour, axis=0)

        # розібратися з єбаними розмірами тих векторів
        # update: розібрався з тими єбаними векторами

        return self.ColourMatrix  # return Matrix of pixels



if __name__ == '__main__':
    New = ImageProcessing('godzilla.jpg', 'nike2.jpg')
    New.showHead()
