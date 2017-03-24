'''
Tool for work with a Image
All images should be the same size

'''
from PIL import Image
import numpy as np


class ImageProcessing(object):
    """

    """
    Wight = 989
    Height = 989

    def __init__(self, *args):  # as INPUT take a list of Images Names
        """
        :param args: # list of Images Names
        """
        self.lenOfPixels = ImageProcessing.Wight * ImageProcessing.Height
        self.listOfImages = list()
        for picture in args:
            self.listOfImages.append(picture.strip())

    def addImages(self, *args):
        """
        :type args: Tuple
        :param args: # list of Images Names
        :return: None
        """
        for picture in args:
            self.listOfImages.append(picture.strip())

    def showHead(self):
        """
        Show 5 head Images from List,
        if List size less than 5 show all Images
        :return: None
        """
        tmp = 5  # number of images to show
        if len(self.listOfImages) < tmp:  # check is number of Images is less than 5
            tmp = len(self.listOfImages)

        for index in range(tmp):  # show top 5 Images
            tmpImage = Image.open(self.listOfImages[index], 'r')
            tmpImage.show()

    def IsValid(self):
        """
        Check all sizes of Images
        :return: None
        """
        for picture in self.listOfImages:
            tmpImg = Image.open(picture, 'r')
            w, h = tmpImg.size
            if w != ImageProcessing.Wight or h != ImageProcessing.Height:
                print("{} has Invalid Size".format(picture))


    def getPixels(self):
        """
        creates Matrix (number of pictures, 989 * 989, 3)
        :return: self.ImagesMatrix - matrix of pixels values for every Image
        """
        self.numOfImages = len(self.listOfImages)  # Nr of images
        self.ImagesMatrix = np.empty((0, self.lenOfPixels, 3),
                                     dtype=np.int32)  # Matrix of pixels values for every picture

        for picture in self.listOfImages:
            tmpPicture = Image.open(picture, 'r')  # Open the Image
            pixelsMatrix = np.array(tmpPicture.getdata())  # create a new numpy array of Picture values
            pixelsMatrix = np.reshape(pixelsMatrix, (1, self.lenOfPixels, 3))  # resize matrix to shape (1, 989 * 989)
            self.ImagesMatrix = np.append(self.ImagesMatrix, pixelsMatrix, axis=0)
        # розібратися з єбаними розмірами тих векторів
        # update: розібрався з тими єбаними векторами

        return self.ImagesMatrix  # return Matrix of pixels


if __name__ == '__main__':
    New = ImageProcessing('godzilla.jpg', 'ggg.jpg')
    New.addImages('godzilla.jpg')
