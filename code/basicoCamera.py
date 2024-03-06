import cv2 as cv
import numpy as np

# Captura o vídeo do canal 0, a câmera
camera = cv.VideoCapture(0)

# Captura cada frame
while True:
    cameraFunct, frame = camera.read()
    cv.imshow("camera frame", frame)

    # Se apertar q, o programa recebe o unicode e para
    if cv.waitKey(1) == ord('q'):
        break


# Podemos manipular o vídeo, alterando os frames como
# alteraríamos imagens
    
camera = cv.VideoCapture(0)
while True:
    cameraFunct, frame = camera.read()
    for linha in frame:
        linha[0:200] = 0, 0, 0
    cv.imshow("camera frame", frame)

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()

