"""
===============================
Dense DAISY feature description
===============================

The DAISY local image descriptor is based on gradient orientation histograms
similar to the SIFT descriptor. It is formulated in a way that allows for fast
dense extraction which is useful for e.g. bag-of-features image
representations.

In this example a limited number of DAISY descriptors are extracted at a large
scale for illustrative purposes.
"""
from skimage.feature import daisy, match_descriptors,plot_matches
from skimage import data
import matplotlib.pyplot as plt


# img = data.camera()
from skimage import io,color
img1 = color.rgb2gray(io.imread('E:/OwnWork/Leaf/TestImage/leafs/leafpgm/leaf1.jpg'))
descs1, descs_img = daisy(img1, step=180, radius=58, rings=2, histograms=6,
                         orientations=8, visualize=True)

img2 = color.rgb2gray(io.imread('E:/OwnWork/Leaf/TestImage/leafs/leafpgm/leaf2.jpg'))
descs2, descs_img = daisy(img2, step=180, radius=58, rings=2, histograms=6,
                         orientations=8, visualize=True)

import numpy as np
x = np.linspace(0,1920,13)[1:-1]
y = np.linspace(0,1080,8)[1:-1]
X,Y = np.meshgrid(x, y)
keypoints1 = np.column_stack((Y.reshape((66)),X.reshape((66))))
keypoints2 = keypoints1

descs1 = descs1.reshape((66,104))
descs2 = descs2.reshape((66,104))
matches12 = match_descriptors(descs1, descs2, cross_check=True,metric='euclidean')


fig, ax = plt.subplots()
plot_matches(ax, img1, img2, keypoints1, keypoints2, matches12)
plt.show()

# fig, ax = plt.subplots()
# ax.axis('off')
# ax.imshow(descs_img)
# descs_num = descs1.shape[0] * descs1.shape[1]
# ax.set_title('%i DAISY descriptors extracted:' % descs_num)
# plt.show()
