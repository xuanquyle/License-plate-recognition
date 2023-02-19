import numpy as np
import cv2
import imutils
import pytesseract
import os
from cv2.cv2 import threshold

try:
    import Image
except ImportError:
    from PIL import Image, ImageEnhance, ImageFilter

class NhanDang():
    def luuAnh(self,c):
        img = cv2.imread(r"E:\S5\CD_HeThongGiaoThongTM\BTL\NhanDangBienSo\CroppedPlate\fileXuLy.png",0)
        cv2.imwrite(r'E:\S5\CD_HeThongGiaoThongTM\BTL\NhanDangBienSo\Collection/' + str(c) + '.png',img)
    def xoaAnh(self,c):
            if os.path.exists('E:\S5\CD_HeThongGiaoThongTM\BTL\license-plate-recognition-master\license-plate-recognition\DuLieuFile/' + str(c) + '.png'):
                os.remove('E:\S5\CD_HeThongGiaoThongTM\BTL\license-plate-recognition-master\license-plate-recognition\DuLieuFile/' + str(c) + '.png')
            else:
                print("The file does not exists")

    def carplate_detect(self,image,carplate_haar_cascade ):
        carplate_overlay = image.copy()
        carplate_rects = carplate_haar_cascade.detectMultiScale(carplate_overlay, scaleFactor=1.1, minNeighbors=3)

        for x, y, w, h in carplate_rects:
            cv2.rectangle(carplate_overlay, (x, y), (x + w, y + h), (255, 0, 0), 5)

            return carplate_overlay

    def carplate_extract(self,image,carplate_haar_cascade):
        carplate_rects = carplate_haar_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

        for x, y, w, h in carplate_rects:
            carplate_img = image[y + 10:y + h - 8,
                           x + 5:x + w - 12]  # Adjusted to extract specific region of interest i.e. car license plate
            return carplate_img

    def enlarge_img(self,image, scale_percent):
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        return resized_image

        ### use Haar Cascade
    # def xuly(self, b):
    #     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #
    #     # Read car image and convert color to RGB
    #     carplate_img = cv2.imread(b)
    #     carplate_img_rgb = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)
    #     cv2.imshow('image', carplate_img_rgb)
    #     carplate_haar_cascade = cv2.CascadeClassifier('plate.xml')
    #
    #
    #
    #     # Setup function to detect car plate
    #     carplate_extract_img = self.carplate_extract(carplate_img_rgb, carplate_haar_cascade)
    #     carplate_extract_img = self.enlarge_img(carplate_extract_img, 130)
    #     carplate_extract_img_gray = cv2.cvtColor(carplate_extract_img, cv2.COLOR_RGB2GRAY)
    #     carplate_extract_img_gray_blur = cv2.medianBlur(carplate_extract_img_gray, 3)  # kernel size 3
    #
    #     #Canny()
    #     # end Canny()
    #
    #     cv2.imshow('image', carplate_extract_img_gray_blur)
    #     cv2.waitKey()
    #     cv2.destroyAllWindows()
    #     # Display the text extracted from the car plate
    #     for i in range(3, 14):
    #         print(f'PSM: {i}')
    #         print(pytesseract.image_to_string(carplate_extract_img_gray_blur,
    #                                     config=f'--psm {i} --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.'))
    #     text=pytesseract.image_to_string(carplate_extract_img_gray_blur,
    #                                       config=f'--psm 6 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.')
    #     texts=text.split('\n')
    #     for t in texts:
    #         if(len(t)>=6):
    #             text=t
    #             break
    #     return text


    ##End Hard casscade
    def xuly1(self,b):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image = cv2.imread(b)

        image = imutils.resize(image, width=500)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 11, 17, 17)

        edged = cv2.Canny(gray, 170, 200)

        cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cv2.imshow('Anh Den trang',gray)
        if(len(cnts)==0):
            return
        img1 = image.copy()
        cv2.imshow('DrawContours',cv2.drawContours(img1, cnts, -1, (0, 255, 0), 3))

        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
        NumberPlateCnt = None

        img2 = image.copy()

        count = 0
        idx = 'fileXuLy'
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # print ("approx = ",approx)
            if len(approx) == 4:  # Select the contour with 4 corners
                NumberPlateCnt = approx  # This is our approx Number Plate Contour

                # Crop those contours and store it in Cropped Images folder
                x, y, w, h = cv2.boundingRect(c)  # This will find out co-ord for plate
                new_img = gray[y:y + h, x:x + w]  # Create new image
                cv2.imwrite('CroppedPlate/' + str(idx) + '.png', new_img)  # Store new image
                # idx+=1

                break
        if(type(NumberPlateCnt)==type(None)):
            return

        cv2.imshow('DrawContoursPlate', cv2.drawContours(image, [NumberPlateCnt], -1, (0, 255, 0), 3))
        cv2.imshow("Cropped License Plate ", new_img)
        # thresh, new_img = cv2.threshold(new_img, 100, maxval=255, type=cv2.THRESH_BINARY)
        for i in range(3, 14):
            print(f'PSM: {i}')
            print(pytesseract.image_to_string(new_img,
                                        config=f'--psm {i} --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.'))
        text = pytesseract.image_to_string(new_img,
                                           config=f'--psm 9 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.')
        return text
    def get_image(self):
        camera = cv2.VideoCapture(0)
        retval , im  = camera.read()
        return im
    def takePhoto(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            live = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ramp_frames = 30
            cv2.imshow("Chup Hinh", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                for i in range(ramp_frames):
                    temp = self.get_image()
                camera_capture = self.get_image()
                file = r"E:\S5\CD_HeThongGiaoThongTM\BTL\NhanDangBienSo\CroppedPlate\fileXuLy.png"
                cv2.imwrite(file, camera_capture)
                break
        cap.release()
        return file


