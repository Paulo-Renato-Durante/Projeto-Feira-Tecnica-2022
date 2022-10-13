
import cv2


def recortaPlaca(imagem):
    
    imagemCinza = deixaCinza(imagem)
    
    imagemBinaria = transformaBinaria(imagemCinza)
    
    #imagemDesfocada = cv2.GaussianBlur(imagemBinaria, (5, 5), 0 )
    #cv2.imshow('draw',imagemBinaria)
    #cv2.waitKey(0)
    contornos = recuperaContornos(imagemBinaria)
    # print(contornos)
    roi = recuperaRoi(contornos, imagem)
    #cv2.imshow('draw',roi)
    #cv2.waitKey(0)
    
    placaAlmentada = almentaPlaca(roi)
    
    return placaAlmentada
    
def deixaCinza(imagem):
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

def transformaBinaria(imagem):
    _, imagemBinaria = cv2.threshold(imagem, 120, 255, cv2.THRESH_BINARY)
    return imagemBinaria



def recuperaContornos(imagem):
    contornos, hier= cv2.findContours(imagem, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contornos

def recuperaRoi(contornos, imagem):
    
    for contorno in contornos:
        
        perimetro = recuperaPerimetro(contorno)
        
        lados = recuperaNumeroLados(contorno, perimetro)

        if perimetro >200:
           
            if (len(lados) == 4):
                
                (x, y ,alt, larg) = recuperaMedidas(contorno)
                roi = imagem[y:y +larg , x-10:x+alt]
                return roi

def recuperaPerimetro(contorno):
    perimetro = cv2.arcLength(contorno , True)
    return perimetro

def recuperaNumeroLados(contorno, perimetro):
    lados = cv2.approxPolyDP(contorno , 0.03 * perimetro,True)
    return lados

def recuperaMedidas(contorno):
    (x, y ,alt, larg) = cv2.boundingRect(contorno)
    return x,y,alt,larg

def almentaPlaca(roi):
    placa = cv2.resize(roi, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    return placa