#pydirectinput.moveTo(300, 150) # Move the mouse to the x, y coordinates 100, 150.
#pydirectinput.click() # Click the mouse at its current location.
#pydirectinput.click(300, 150) # Click the mouse at the x, y coordinates 200, 220.
#pydirectinput.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
#pydirectinput.doubleClick() # Double click the mouse at the
#pydirectinput.press('esc') # Simulate pressing the  Escape key.


import pyautogui,time,PIL
import cv2,os
import numpy as np

import time
from  pydirectinput import keyDown,keyUp
import keyboard as key
from veri_seti_duzenle import duzenle

from ALEX_NET import NET
import torch
from tqdm import tqdm
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from threading import Thread

device=torch.device(0)

class MODEL_NET():
    def __init__(self):
        
        self.MODEL_NAME = None
        
        self.model_belirle()
        self.network()

    def model_belirle(self):
        print("isim aliniyorr ...",end="\n\n")
        time.sleep(2)
        yol=os.listdir("MODELLER\\tek")
        print("""

________________  MODEL SEÇİMİNİ YAP __________


""")
        for s,i in enumerate(yol):
            print(f"\t[{s+1}] {i}")

        print("""

_______________________________________________


"""     )

        sec=int(input("=>> " ))

        self.MODEL_NAME="MODELLER\\tek\\"+yol[sec-1]
        print(self.MODEL_NAME,"model secildi",end="\n\n")
        time.sleep(2)

    def network(self):
        print("\n\nmodel çagiriliyor...",end="\n\n")
        time.sleep(2)
        
        
        
        model=NET().to(device)
        model.load_state_dict(torch.load(self.MODEL_NAME))

        optimizer=optim.Adam(model.parameters(),lr=1e-4)
        lossf = nn.MSELoss()

        self.menu(model)

    def menu(self,model):
        print("tahmin işleminin başlamasına ;",end="\n\n")
        time.sleep(2)
        
        for i in range(5)[::-1]:
            print(">",i)
            time.sleep(1)
        print("\n ____ BAŞLADI ____",end="\n\n")
        
            
        while True:
            resim=np.array(pyautogui.screenshot(region=(0,112,860,428)))
            
            siyah,img=self.siyah_beyaz(resim)
            
            x=torch.Tensor(img).view(-1,1,86,86).to(device)
            x=x/255.0

            pred=model(x)
            self.tahmin(torch.argmax(pred))
            print(pred,end="\n\n")
            
            al = Thread(target=cv2.imshow("siyah_beyaz",siyah))
            al.start()
            if cv2.waitKey(25) & 0xFF == ord("q") or key.is_pressed('t'):
                keyUp("w")
                keyUp("a")
                keyUp("d")
                print("\n\n devap etmek için b ye basın",end="\n\n")
                while True:
                    if key.is_pressed('b'):
                        break
                

    def tahmin(self,pred):
        #AWD
        
        ############################## sağa
        if pred==0:
            keyDown("a")
            keyUp("w")
            keyUp("d")
            keyUp("s")
        ############################# ileri
        elif pred==1:
            keyDown("w")
            keyUp("a")
            keyUp("d")
            keyUp("s")
        ############################ sola
        elif pred==2:
            keyDown("d")
            keyUp("w")
            keyUp("a")
            keyUp("s")
        ########################### sag ileri
        elif pred==3:
            keyDown("w")
            keyDown("a")
            keyUp("d")
            keyUp("s")
        ########################### sol ileri
        elif pred==4:
            keyDown("w")
            keyDown("d")
            keyUp("a")
            keyUp("s")
        ########################### arka
        elif pred==5:
            keyDown("s")
            keyUp("d")
            keyUp("w")
            keyUp("a")
        ########################## sag arka
        elif pred==6:
            keyDown("s")
            keyDown("a")
            keyUp("w")
            keyUp("d")
            
        ########################### sol arka
        elif pred==7:
            keyDown("s")
            keyDown("d")
            keyUp("w")
            keyUp("a")
    def maskeleme(self,img,vertices):
        mask=np.zeros_like(img)
        cv2.fillPoly(mask,vertices,255)
        masked=cv2.bitwise_and(img,mask)
        return masked

    def siyah_beyaz(self,image):
        siyah=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        #siyah=cv2.Canny(siyah,threshold1=400,threshold2=200)
        siyah=cv2.Laplacian(siyah,cv2.CV_8U)
        #siyah=cv2.Laplacian(siyah,cv2.CV_8UC3)
        # burdan sonrası maskeleme
        vertices=np.array([[0,900],[0,300],[0,600],[0,150],[2000,200],[0,900]])
        kısalt=self.maskeleme(siyah,[vertices])
        
        kısalt=cv2.resize(kısalt,(86,86))
        
        
        # burası cızgı bulma algorıtması ıcın
        #line=cv2.HoughLinesP(siyah,1,np.pi/180,180,20,15)
        #siyah=cv2.GaussianBlur(siyah,(5,5),0)
        return siyah,kısalt

if __name__=="__main__":
    netvork=MODEL_NET()
