import cv2
from matplotlib import pyplot as plt
import numpy as np
from IPython.display import Image

img_tenis = cv2.imread("res/actividad2/bola.png", cv2.IMREAD_COLOR)
# Img rgb
img_rgb = cv2.cvtColor(img_tenis, cv2.COLOR_BGR2RGB)
# Img hsv
img_hsv = cv2.cvtColor(img_tenis, cv2.COLOR_BGR2HSV)
# Img XYZ
img_xyz = cv2.cvtColor(img_tenis, cv2.COLOR_BGR2XYZ)
# LAB
img_lab = cv2.cvtColor(img_tenis, cv2.COLOR_BGR2LAB)

fig, axs = plt.subplots(4, 3, figsize=(10, 10))
# R
axs[0, 0].imshow(img_rgb[:,:,0], cmap="gray")
axs[0, 0].set_title("R")
# G
axs[0, 1].imshow(img_rgb[:,:,1], cmap="gray")
axs[0, 1].set_title("G")
# B
axs[0, 2].imshow(img_rgb[:,:,2], cmap="gray")
axs[0, 2].set_title("B")
# H
axs[1, 0].imshow(img_hsv[:,:,0], cmap="gray")
axs[1, 0].set_title("H")
# S
axs[1, 1].imshow(img_hsv[:,:,1], cmap="gray")
axs[1, 1].set_title("S")
# V
axs[1, 2].imshow(img_hsv[:,:,2], cmap="gray")
axs[1, 2].set_title("V")
# X
axs[2, 0].imshow(img_xyz[:,:,0], cmap="gray")
axs[2, 0].set_title("X")
# Y
axs[2, 1].imshow(img_xyz[:,:,1], cmap="gray")
axs[2, 1].set_title("Y")
# Z
axs[2, 2].imshow(img_xyz[:,:,2], cmap="gray")
axs[2, 2].set_title("Z")
# L
axs[3, 0].imshow(img_lab[:,:,0], cmap="gray")
axs[3, 0].set_title("L")
# A
axs[3, 1].imshow(img_lab[:,:,1], cmap="gray")
axs[3, 1].set_title("A")
# B
axs[3, 2].imshow(img_lab[:,:,2], cmap="gray")
axs[3, 2].set_title("B")
plt.show()
"""
Los canales donde mejor se puede reconocer la pelota son el A y B del formato LAB, ya que presentan una mayor diferencia entre el fondo y la pelota
"""

img_tigre = cv2.imread("res/actividad2/tigre.png",cv2.IMREAD_COLOR)
img_tigre_rgb = cv2.cvtColor(img_tigre,cv2.COLOR_BGR2RGB)
# Img rgb
img_tigre_rgb = cv2.cvtColor(img_tigre, cv2.COLOR_BGR2RGB)
# Img hsv
img_tigre_hsv = cv2.cvtColor(img_tigre, cv2.COLOR_BGR2HSV)
# Img XYZ
img_tigre_xyz = cv2.cvtColor(img_tigre, cv2.COLOR_BGR2XYZ)
# LAB
img_tigre_lab = cv2.cvtColor(img_tigre, cv2.COLOR_BGR2LAB)


fig, axs = plt.subplots(4, 3, figsize=(10, 10))
# R
axs[0, 0].imshow(img_tigre_rgb[:,:,0], cmap="gray")
axs[0, 0].set_title("R")
# G
axs[0, 1].imshow(img_tigre_rgb[:,:,1], cmap="gray")
axs[0, 1].set_title("G")
# B
axs[0, 2].imshow(img_tigre_rgb[:,:,2], cmap="gray")
axs[0, 2].set_title("B")
# H
axs[1, 0].imshow(img_tigre_hsv[:,:,0], cmap="gray")
axs[1, 0].set_title("H")
# S
axs[1, 1].imshow(img_tigre_hsv[:,:,1], cmap="gray")
axs[1, 1].set_title("S")
# V
axs[1, 2].imshow(img_tigre_hsv[:,:,2], cmap="gray")
axs[1, 2].set_title("V")
# X
axs[2, 0].imshow(img_tigre_xyz[:,:,0], cmap="gray")
axs[2, 0].set_title("X")
# Y
axs[2, 1].imshow(img_tigre_xyz[:,:,1], cmap="gray")
axs[2, 1].set_title("Y")
# Z
axs[2, 2].imshow(img_tigre_xyz[:,:,2], cmap="gray")
axs[2, 2].set_title("Z")
# L
axs[3, 0].imshow(img_tigre_lab[:,:,0], cmap="gray")
axs[3, 0].set_title("L")
# A
axs[3, 1].imshow(img_tigre_lab[:,:,1], cmap="gray")
axs[3, 1].set_title("A")
# B
axs[3, 2].imshow(img_tigre_lab[:,:,2], cmap="gray")
axs[3, 2].set_title("B")
plt.show()

"""
Los canales donde se puede reconocer mejor al tigure son el S del formato HSV y el B del formato LAB, en el primero incluye un mayor reconocimiento
del tigre (incluyendo sus rayas) pero un fono un poco mas claro, por otro lado el B distingue mas al tigre del fondo, de una manera
mas uniforme pero incluye menos partes del tigre 
"""
