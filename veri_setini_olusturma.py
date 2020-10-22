import pyautogui,time
import cv2,os
import numpy as np
import matplotlib.pyplot as plt

import time
import keyboard as key

class veri():
    def __init__(self):
        self.dur=False
        self.başla=None
        self.say=1
        
        self.train_list=[]

        self.menu()
        
    def menuler(self,menu="anamenu"):
        if menu == "anamenu":
            print( """

        #######################################################################

                YAPAY ZEKA İCİN VERİ TOPLAYIN

                    [ r ]  yeni oyun
                          _______________________________
                          |_________ oyun içi __________|
                          |                             |
                          |    [ t ] duraklat           |
                          |                             |
                          |        [ y ] devam et       |
                          |                             |
                          |    [ q ] çıkış              |
                          |_____________________________|
                    
                    
                              [ q ]  çikiş
                    

        #########################################################################


        """)
        elif menu=="içerik":
            print("""
                        
                    _______________________________
                    |_________ oyun içi __________|
                    |                             |
                    |    [ t ] duraklat           |
                    |                             |
                    |        [ y ] devam et       |
                    |                             |
                    |    [ q ] çıkış              |
                    |_____________________________|
                    
                        beklemede ...""")
    def isim(self):
        print("isim aliniyorr ...",end="\n\n")
        time.sleep(2)
        yol=os.listdir("veri_setleri")
        
        for i in range(1,1000):
            name=f"train_siyah_beyaz_{i}.npy"

            if name not in yol:
                self.başla=name
                break
            else:
                pass

    def basla(self):
        #region=(0,100,860,440)
        
        while True:
            resim=np.array(pyautogui.screenshot(region=(0,125,1920,970)))
            resim=cv2.resize(resim,(860,440))
            siyah=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
            
            klavye=self.bak()

            self.train_list.append([siyah,klavye])
            if len(self.train_list)%50==0:
                print(str(self.say)+". paket kaydedildi.")
                self.say+=1
            if key.is_pressed('t'):
                self.menuler(menu="içerik")
                while True:
                    if key.is_pressed('y'):
                        break
                    elif key.is_pressed('q'):
                        self.dur=True
                        print(" ana menuye donuluyor ..",end="\n\n")
                        time.sleep(2)
                        break
                print("devam edildi..",end="\n\n")
            if cv2.waitKey(25) & 0xFF==ord("q") or key.is_pressed('q') or self.dur==True:
                print("\n\n paketler kaydediliyor ... ",end="\n\n")
                np.save(f"veri_setleri\\"+self.başla,np.array(self.train_list))
                print(str(self.say)+" tane  paket kaydedildi.")
                time.sleep(2)
                cv2.destroyAllWindows()
                break
    def bak(self):
        #[A,W,D,aw,dw,s,as,sd]
        if key.is_pressed('a'):
            anahtar=[1,0,0]
            
        elif key.is_pressed('w'):
            anahtar=[0,1,0]
            
        elif key.is_pressed('d'):
            anahtar=[0,0,1]
            
        else:
            anahtar=[0,0,0]

        """
        anahtar=[0,0,0,0,0,0,0,0]
        
        if key.is_pressed('a'):
            anahtar=[1,0,0,0,0,0,0,0]
            
        if key.is_pressed('w'):
            anahtar=[0,1,0,0,0,0,0,0]
            
        if key.is_pressed('d'):
            anahtar=[0,0,1,0,0,0,0,0]
            
        if key.is_pressed('w') and key.is_pressed('d'):
            anahtar=[0,0,0,0,1,0,0,0]
            
        if key.is_pressed('a') and key.is_pressed('w'):
            anahtar=[0,0,0,1,0,0,0,0]
            
        if key.is_pressed('s'):
            anahtar=[0,0,0,0,0,1,0,0]
            
        if key.is_pressed('a') and key.is_pressed('s'):
            anahtar=[0,0,0,0,0,0,1,0]
            
        if key.is_pressed('s') and key.is_pressed('d'):
            anahtar=[0,0,0,0,0,0,0,1]
        
            
        """
        return anahtar

    def menu(self):
        while True:
            self.isim()
            self.menuler()
            print("yeni veri kumesi ismi : ",self.başla,end="\n\n")
            a=input("==>> ")
            if a=="r":
                print("veri kumesi ismi : ",self.başla,end="\n\n")
                time.sleep(1)
                self.train_list=[]
                self.say=1
                self.dur=False
                print("parametreler ayarlanıyor .. ",end="\n\n")
                time.sleep(2)
                print("başlamaya ; \n")
                for i in range(5)[::-1]:
                    time.sleep(1)
                    print("> ",i)
                print("\n___  BAŞLADI ___ ")
                self.basla()
            elif a == "q":
                print("çıkılıyor ..")
                time.sleep(2)
                break
            else:
                pass


if __name__=="__main__":
    
    data=veri() 










