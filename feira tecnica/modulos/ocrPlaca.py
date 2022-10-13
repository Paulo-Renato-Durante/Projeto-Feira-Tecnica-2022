


import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\Tesseract.exe'

def ocrPlaca(imagem):
    imagemCinza = deixaCinza(imagem)
    imagemBinaria = transformaBinaria(imagemCinza) 
    placaTexto = lePlaca(imagemBinaria)
    placaLimpa = limpaTexto(placaTexto)
    return placaLimpa
    
    
    
def deixaCinza(imagem):
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

def transformaBinaria(imagem):
    _, imagemBinaria = cv2.threshold(imagem, 90, 255, cv2.THRESH_BINARY)
   # cv2.imshow('imagemBinaria', imagemBinaria)
    return imagemBinaria

def lePlaca(imagem):
    config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ023456789 --psm 6'
    
    placa = pytesseract.image_to_string(imagem, lang='eng', config=config)
    return placa

def limpaTexto(placa):
    placaLimpa = placa[-8:]
    return placaLimpa

