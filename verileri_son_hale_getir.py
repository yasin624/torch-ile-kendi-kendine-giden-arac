import numpy as np
import time,os,tqdm,cv2
from random import shuffle


class birleştir():
    def __init__(self):
         self.veriler=None

         self.veri_çek()
         self.kaydet()
         self.sil()
    
    
    def veri_çek(self):
        yol=os.listdir("veri_setleri\\onbellek")
        print("veri setleri belirleniyor.. ",end="\n\n")
        time.sleep(2)
            
        print(f"""       veri set dosyalarınız ;
    __________________________________________
         """
            )
        print("\t",*yol,sep="\n\t")

        print("""
        _______________________________________
        
            """
            )
        print(" veriler cekiliyor .. ",end="\n\n")
        time.sleep(2)
        for i in tqdm.tqdm(range(len(yol))):
            
            if yol[i].startswith("duzelt"):
                if self.veriler == None:
                    self.veriler=np.load("veri_setleri\\onbellek\\"+yol[i],allow_pickle=True)
                else:
                    veri=np.load("veri_setleri\\onbellek\\"+yol[i],allow_pickle=True)
                    self.veriler=np.concatenate((self.veriler,veri))
            else:
                pass

        
        print("\n\n")

        print("çekilen toplam veri seti : ",len(self.veriler),end="\n\n")

        

        
    def kaydet(self):
        print("toplam da işlenebişlecek veri seti : ",len(self.veriler),end="\n\n")
        print("veriler kaydediliyor ...",end="\n\n")
        yol=os.listdir("duzeltiliş_veriler")
            
        for i in range(1,1000):
            if f"train_data_{i}.npy" not in yol:
                np.save(f"duzeltiliş_veriler\\train_data_{i}.npy",self.veriler)
                break
            else:
                pass
        time.sleep(2)
        print(f"train_data_{i}.npy verisi kaydedildi.",end="\n\n")

        
    def sil(self):
        yol=os.listdir("veri_setleri\\onbellek")
        print("artıklar temizleniyor .. ",end="\n\n")
        time.sleep(2)
        if len(yol)>0:
            for i in range(len(yol)):
                if yol[i].startswith("duzelt"):
                    os.remove("veri_setleri\\onbellek\\"+yol[i])
                    print(yol[i]+" dosyası temizlendi..",end="\n\n")
                    time.sleep(2)
        print(f"{yol[i]} veri seti temizlendi ve kaydedildi.",end="\n\n")
        time.sleep(2)

if __name__ =="__main__":
    bosalt=birleştir()
    
