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
#print(pytesseract.image_to_boxes(img))
#wyprintujmy w konsoli co jest na obrazku
#print(pytesseract.image_to_string(img))
# zobaczmy obrazek
#cv2.imshow('Result', img)
# opoznimy wyswietlanie obrazka do nieskoczonosci :)
#cv2.waitKey(0)


#### Detecting Characters  ######
#############################################
#hImg, wImg,_ = img.shape
#infunkci formacje z image_to_boxes zapiszmy w boxes
#boxes = pytesseract.image_to_boxes(img)
# stworzmy funkcje która dla kazdego b w boxes bedzie
# printowała położenie punktów
#for b in boxes.splitlines():
    #print(b)
    #transformujemy na liste by moc dostac sie do kazdego elementu
    #b = b.split(' ')
    #print(b)
    ## konwertujemy x, y, w, h na int i kazdemu z punktów b przypisujemy
    #cyfry od 1 do 4
    #x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    #rysujemy rectangle i dodajemy tekst
    #cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
    #cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)


#### Detecting Words  ######
#############################################
hImg, wImg,_ = img.shape
#tylko cyfry
cong = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(img,config=cong)
#print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        print(b)
        if len(b)==12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x,y),(w+x,h+y),(0, 0, 255),3)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)


cv2.imshow('result',img)
cv2.waitKey(0)




