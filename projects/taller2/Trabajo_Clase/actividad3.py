import cv2
from matplotlib import pyplot as plt
import numpy as np
from IPython.display import Image

img = cv2.imread("res/actividad2/tigre.png", cv2.IMREAD_COLOR)
# Img rgb
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_yuv = img_rgb.copy()
# Calcular YUV
img_yuv[:,:,0] = 0.299*img_rgb[:,:,0] + 0.587*img_rgb[:,:,1] + 0.114*img_rgb[:,:,2]
img_yuv[:,:,1] = -0.147*img_rgb[:,:,0] + 0.289*img_rgb[:,:,1] + 0.436*img_rgb[:,:,2]
img_yuv[:,:,2] = 0.615*img_rgb[:,:,0] - 0.515*img_rgb[:,:,1] - 0.100*img_rgb[:,:,2]

fig, axs = plt.subplots(1, 3, figsize=(10, 10))
# Y
axs[0].imshow(img_yuv[:,:,0], cmap="gray")
axs[0].set_title("Y")
# U
axs[1].imshow(img_yuv[:,:,1], cmap="gray")
axs[1].set_title("U")
# V
axs[2].imshow(img_yuv[:,:,2], cmap="gray")
axs[2].set_title("V")
plt.show()


img_pato = cv2.imread("res/actividad1/pato.jpg", cv2.IMREAD_COLOR)
# Img rgb
img_pato_rgb = cv2.cvtColor(img_pato, cv2.COLOR_BGR2RGB)
img_pato_yuv = img_pato_rgb.copy()
# Calcular YUV
img_pato_yuv[:,:,0] = 0.299*img_pato_rgb[:,:,0] + 0.587*img_pato_rgb[:,:,1] + 0.114*img_pato_rgb[:,:,2]
img_pato_yuv[:,:,1] = -0.147*img_pato_rgb[:,:,0] + 0.289*img_pato_rgb[:,:,1] + 0.436*img_pato_rgb[:,:,2]
img_pato_yuv[:,:,2] = 0.615*img_pato_rgb[:,:,0] - 0.515*img_pato_rgb[:,:,1] - 0.100*img_pato_rgb[:,:,2]

fig, axs = plt.subplots(1, 3, figsize=(10, 10))
# Y
axs[0].imshow(img_pato_yuv[:,:,0], cmap="gray")
axs[0].set_title("Y")
# U
axs[1].imshow(img_pato_yuv[:,:,1], cmap="gray")
axs[1].set_title("U")
# V
axs[2].imshow(img_pato_yuv[:,:,2], cmap="gray")
axs[2].set_title("V")
plt.show()