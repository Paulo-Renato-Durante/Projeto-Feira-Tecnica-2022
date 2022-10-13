import cv2
import modulos.recorta_placa as RP
import modulos.ocrPlaca as ocr
def placa(placa):

    imagem = cv2.imread(placa)

    #cv2.imshow('draw', imagem)
    #cv2.waitKey(0)

    placaImagem = RP.recortaPlaca(imagem)
    #cv2.imshow('draw', placaImagem)
    #cv2.waitKey(0)


    placaTexto= ocr.ocrPlaca(placaImagem)
    return placaTexto


 
