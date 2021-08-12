import cv2
import pytesseract


# Podajemy scieżkę do lokacji gdzie została zainsatlowana biblioteka
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# Podajmy sciezke do obrazka
img = cv2.imread('4.png')
# Konwersja z BGR(vc2) na RGB(tesseract)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#skąd wiedzieć gdzie znajduja się litery i cyfry na obrazku
# i jaki jest ich rozmiar?
print(pytesseract.image_to_boxes(img))
#wyprintujmy w konsoli co jest na obrazku
print(pytesseract.image_to_string(img))
# zobaczmy obrazek
cv2.imshow('Result', img)
# opoznimy wyswietlanie obrazka do nieskoczonosci :)
cv2.waitKey(0)