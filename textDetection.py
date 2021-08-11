import cv2
import pytesseract


# Podajemy scieżkę do lokacji gdzie została zainsatlowana biblioteka
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# Podajmy sciezke do obrazka
img = cv2.imread('3.png')
# Konwersja z BGR(vc2) na RGB(tesseract)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# zobaczmy obrazek
cv2.imshow('Result', img)
# opoznimy wyswietlanie obrazka do nieskoczonosci :)
cv2.waitKey(0)

