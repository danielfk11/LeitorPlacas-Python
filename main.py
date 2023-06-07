import cv2
import pytesseract
import sqlite3

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def verificar_placa(placa):
    cursor.execute("SELECT * FROM moradores WHERE placa = ?", (placa,))
    result = cursor.fetchone()

    if result:
        print("Placa encontrada no banco de dados!")
        print("Portao Aberto!")

def ler_texto(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    texto = pytesseract.image_to_string(binary)

    return texto

def extrair_placas(texto):
    placas = []
    palavras = texto.split()
    for palavra in palavras:
        if len(palavra) == 7 and palavra.isalnum():
            placas.append(palavra)
    return placas

def exibir_webcam():
    video_capture = cv2.VideoCapture(0)

    while True:

        ret, frame = video_capture.read()
        texto = ler_texto(frame)
        print("Texto encontrado:", texto)
        placas = extrair_placas(texto)

        if placas:
            for placa in placas:
                verificar_placa(placa)

        #camera para procurar AQUI
        cv2.imshow('Webcam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    conn.close()

# cham princ
exibir_webcam()
