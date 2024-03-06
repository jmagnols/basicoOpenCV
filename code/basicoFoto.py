import cv2 as cv
import numpy as np

#################

# Ler e mostrar imagem
image = cv.imread('fotos/coruja.jpg')

# Dimensões da imagem, para a imagem caber na tela
dimensoes = int(image.shape[1] * 0.30), int(image.shape[0] * 0.30) 
image = cv.resize(image, dimensoes, interpolation = cv.INTER_AREA)

#cv.imshow('Coruja', image)
cv.waitKey(0)

#################

# Uma imagem é um array de pixeis
canvas = np.zeros((500, 500, 3))

#cv.imshow('Canvas vazio', canvas)
cv.waitKey(0)

# Criamos um canvas todo de pixeis pretos.
# Vamos fazer parte dele ser de outra cor.

# Pixeis de 100 a 250 verticalmente e 300 de 450 horizontalmente
canvas[100:250, 300: 450] = 0, 255, 0

#cv.imshow('Canvas com detalhe', canvas)
cv.waitKey(0)

# cv.rectangle faz isso mais facilmente
canvas = cv.rectangle(canvas, (100,250), (300,450), (0,255,0), thickness = 4)

#cv.imshow('Canvas com borda retangular', canvas)
cv.waitKey(0)

# Repare que agora a imagem tem as duas "edições" que fizemos no array

#################


