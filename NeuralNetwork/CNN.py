
import tensorflow as tf
import numpy as np
from ImageClass import ImageProcessing as imgp

Images = imgp('godzilla.jpg', 'nike2.jpg', 'Nike.jpg')
X = tf.placeholder(tf.float32, [None, imgp.inputLen])