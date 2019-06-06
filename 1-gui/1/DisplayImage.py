import numpy as np
import cv2
from matplotlib import pyplot as plt



# Load an color image in grayscale
img = cv2.imread('photo_2019-05-22_21-47-11.jpg',0)

# resize image to normal
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# save image in folder with Name given
cv2.imwrite('messigray.png',img)

# show image
cv2.imshow('image',img)

# w8 until one kry selected can use it for if or el 
k = cv2.waitKey(0)

# destroy pics
cv2.destroyAllWindows()


# usnig matplotlib to show image
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
cv2.waitKey()