import cv2
import pytesseract


# Podajemy scieżkę do lokacji gdzie została zainsatlowana biblioteka
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# Podajmy sciezke do obrazka
img = cv2.imread('4.png')
# Konwersja z BGR(vc2) na RGB(tesseract)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



#### Detecting Characters  ######
#############################################
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    print(b)
    #transformujemy na liste by moc dostac sie do kazdego elementu
    b = b.split(' ')
    ## konwertujemy x, y, w, h na int i kazdemu z punktów b przypisujemy
    #cyfry od 1 do 4
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    #rysujemy rectangle i dodajemy tekst
    cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
    cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)


cv2.imshow('result',img)
cv2.waitKey(0)