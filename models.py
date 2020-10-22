import numpy as np
from ALEX_NET import NET
import cv2,time,os
from tqdm import tqdm
from veri_seti_duzenle import duzenle
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch




class NETWORK():
    def __init__(self):
        self.duz=duzenle()
        
        self.WIDTH = self.duz.WIDTH
        self.HEIGHT = self.duz.HEIGHT
        self.LR = self.duz.LR
        self.EPOCHS = 3
        self.BACH_SİZE=128
        
        self.MODEL_NAME = None
        self.train_data=None

        # model GPU ile eğitilecegini soylüyor
        self.device=torch.device(0)
        print(self.device)
        
        self.isim()
        self.veri_belirle()
        self.model_kayıt()
        
    def veri_belirle(self):
        print("veriler  aliniyorr ...",end="\n\n")
        time.sleep(2)
        yol=os.listdir("duzeltiliş_veriler")
        
        print("""

________________  HANGİ VERİYİ EYİTECEN SEÇİMİNİ YAP __________


""")
        for s,i in enumerate(yol):
            print(f"\t[{s+1}] {i}")

        print("""

_______________________________________________________________


"""     )

        sec=int(input("=>> " ))
        time.sleep(2)

        self.veri_al(yol[sec-1])



    
    def isim(self):
        print("\n\nMODEL isim aliniyorr ...",end="\n\n")
        time.sleep(2)
        yol=os.listdir("MODELLER\\tek")
        
        for i in range(1,1000):
            name=f"car_model_torc_{i}.model"

            if name not in yol:
                self.MODEL_NAME=name
                
                break
            else:
                pass
        print("model ismi : ",self.MODEL_NAME,end="\n\n")
        time.sleep(2)
        
    def veri_al(self,veri_ismi):
        print(f"\n\n {veri_ismi}  veri seti aliniyor...",end="\n\n")
        time.sleep(2)
        self.train_data = np.load("duzeltiliş_veriler\\"+veri_ismi,allow_pickle=True)

        
        self.network(self.train_data)
        
    def network(self,data):
        print("model çagiriliyor...",end="\n\n")
        time.sleep(2)

        self.model = NET().to(self.device)
        print(self.model)
        time.sleep(2)

        # optimizasyon fonksiyonları
        self.optimizer=optim.Adam(self.model.parameters(),lr=1e-4)
        self.lossf = nn.MSELoss()
        
        boyut=int(len(data)*0.1)
        train = data[:-boyut]
        test = data[-boyut:]

        print("\n\n eyitim kümesi : ",len(train),end="\n\n")
        print(" test  kümesi : ",len(test),end="\n\n")

        print("___________________________________________________________________",end="\n\n")

        self.veri_hazırla(train,test)

    def veri_hazırla(self,train,test):
        
        print("veri hazırlanıyor ...",end="\n\n")
        time.sleep(2)
        X = torch.Tensor([i[0] for i in train]).view(-1,1,86,86)
        Y = torch.Tensor([i[1] for i in train])
        X = X/255.0

        

        test_x = torch.Tensor([i[0] for i in test]).view(-1,1,86,86)
        test_x = test_x/255.0
        test_y = torch.Tensor([i[1] for i in test])

        self.model_eğit(X,Y,test_x,test_y)
        
        
    def model_eğit(self,X,Y,test_x,test_y):
        print("model eğitiliyor...",end="\n\n")
        time.sleep(2)

        for epoch in range(self.EPOCHS):
            for i in tqdm(range(0,len(X),self.BACH_SİZE)):
                bach_x=X[i:i+self.BACH_SİZE].to(self.device)
                bach_y=Y[i:i+self.BACH_SİZE].to(self.device)

                self.model.zero_grad()

                pred=self.model(bach_x)

                loss=self.lossf(pred,bach_y)

                loss.backward()

                self.optimizer.step()
                
            self.tahmin_verisi_dogruluğu(epoch,test_x,test_y)

    def tahmin_verisi_dogruluğu(self,epoch,test_x,test_y):
        dogru=0
        top=0

        with torch.no_grad():
            for i in tqdm(range(len(test_x))):
                x=torch.Tensor(test_x[i]).view(-1,1,86,86).to(self.device)

                pred=self.model(x)

                if torch.argmax(pred) == torch.argmax(test_y[i]):
                    dogru+=1
                top+=1

        accury=(dogru/top)*100

        print(f"{epoch} ) accury : ",accury)

        self.model_en_iyi_dogruluğu(accury)
        
    def model_en_iyi_dogruluğu(self,accury):
        self.dogru_model=None
        dogruluk=None

        if self.dogru_model != None:
            if dogruluk <accury:
                self.dogru_model=self.model.state_dict()
                dogruluk=accury
        else:
            self.dogru_model=self.model.state_dict()
            dogruluk=accury
        
    def model_kayıt(self):
        
        print(f"\n\n{self.MODEL_NAME} modelli kaydediliyor...",end="\n\n")
        time.sleep(2)
        torch.save(self.dogru_model,"MODELLER\\tek\\"+self.MODEL_NAME)
        print("model kaydedildi...",end="\n\n")
        time.sleep(2)
        
if __name__=="__main__":      
    net=NETWORK()





