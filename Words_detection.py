import cv2
import pytesseract


# Podajemy scieżkę do lokacji gdzie została zainsatlowana biblioteka
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# Podajmy sciezke do obrazka
img = cv2.imread('4.png')
# Konwersja z BGR(vc2) na RGB(tesseract)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#### Detecting Words  ######
#############################################
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_data(img)
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
