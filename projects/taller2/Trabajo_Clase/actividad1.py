import cv2
from matplotlib import pyplot as plt
import numpy as np
from IPython.display import Image

img_pato = cv2.imread("res/actividad1/pato.jpg", cv2.IMREAD_COLOR)
img_pato = cv2.cvtColor(img_pato, cv2.COLOR_BGR2RGB)
img_gato = cv2.imread("res/actividad1/gato.jpg",cv2.IMREAD_COLOR)
img_gato = cv2.cvtColor(img_gato, cv2.COLOR_BGR2RGB)

plt.imshow(img_pato)
plt.show()
plt.imshow(img_gato)
plt.show()

img_pato[0:img_pato.shape[0]//2, 0:img_pato.shape[1]//2,0] = 0
img_pato[0:img_pato.shape[0]//2, 0:img_pato.shape[1]//2,2] = 0
"""Colombia"""
q1_pato= img_pato[0:img_pato.shape[0]//2,img_pato.shape[1]//2:]
# amarillo 
q1_pato[0:q1_pato.shape[0]//3,:] = (225,225,0)
# azul
q1_pato[q1_pato.shape[0]//3:q1_pato.shape[0]*2//3,:] = (0,0,225)
#Rojo
q1_pato[q1_pato.shape[0]*2//3:q1_pato.shape[0]*3//3,:] = (225,0,0)
"""Alemania"""
q3_pato = img_pato[img_pato.shape[0]//2:, 0:img_pato.shape[1]//2]
#negro
q3_pato[0:q3_pato.shape[0]//3,:] = (0,0,0)
#rojo
q3_pato[q3_pato.shape[0]//3:q3_pato.shape[0]*2//3,:] = (225,0,0)
#Amarillo
q3_pato[q3_pato.shape[0]*2//3:q3_pato.shape[0]*3//3,:] = (225,225,0)
plt.imshow(img_pato)
plt.show()

img_gato[0:img_gato.shape[0]//2, 0:img_gato.shape[1]//2,0] = 0
img_gato[0:img_gato.shape[0]//2, 0:img_gato.shape[1]//2,2] = 0
"""Italia"""
q1_gato = img_gato[:img_gato.shape[0]//2, img_gato.shape[1]//2:]
#Verde
q1_gato[:,:q1_gato.shape[1]//3] = (8,149,76)
#Blanco
q1_gato[:,q1_gato.shape[1]//3:q1_gato.shape[1]*2//3] = (225,225,225)
#Rojo
q1_gato[:,q1_gato.shape[1]*2//3:q1_gato.shape[1]*3//3] = (225,0,0)
"""Russia"""
q3_gato = img_gato[img_gato.shape[0]//2:,:img_gato.shape[1]//2]
#negro
q3_gato[0:q3_gato.shape[0]//3,:] = (225,225,225)
#rojo
q3_gato[q3_gato.shape[0]//3:q3_gato.shape[0]*2//3,:] = (0,0,225)
#Amarillo
q3_gato[q3_gato.shape[0]*2//3:q3_gato.shape[0]*3//3,:] = (225,0,0)
plt.imshow(img_gato)
plt.show()