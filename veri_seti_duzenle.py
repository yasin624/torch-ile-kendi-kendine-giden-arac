import numpy as np
import cv2,time,os,tqdm
from random import shuffle
import verileri_son_hale_getir



class duzenle():

    def __init__(self):
        self.data=None
        self.clear_data=[]
        self.WIDTH = 86
        self.HEIGHT = 86
        self.LR = 1e-3
        self.EPOCHS =5

        self.lefts=[]
        self.rights=[]
        self.go=[]
        """
        self.arka=[]
        self.leftgo=[]
        self.rightgo=[]
        self.leftarka=[]
        self.rightarka=[]
        """
        
    def veri_al(self,yol):
        self.data=np.load("veri_setleri\\"+yol,allow_pickle=True)
        
        print("\n\n")

        print("çekilen toplam veri seti : ",len(self.data),end="\n\n")
        
    def maskeleme(self,img,vertices):
        mask=np.zeros_like(img)
        cv2.fillPoly(mask,vertices,255)
        masked=cv2.bitwise_and(img,mask)
        return masked

    def siyah_beyaz(self,img):
        #siyah=cv2.Canny(img,threshold1=400,threshold2=200) 
        siyah=cv2.Laplacian(img,cv2.CV_8U)
        #siyah=cv2.Laplacian(siyah,cv2.CV_8UC3)
        
        # burdan sonrası maskeleme
        vertices=np.array([[0,900],[0,300],[0,600],[0,150],[2000,200],[0,900]])
        siyah=self.maskeleme(siyah,[vertices])
        
        siyah=cv2.resize(siyah,(self.WIDTH,self.HEIGHT))
        
        # burası cızgı bulma algorıtması ıcın
        #line=cv2.HoughLinesP(siyah,1,np.pi/180,180,20,15)
        #siyah=cv2.GaussianBlur(siyah,(5,5),0)
        return siyah

    def gorsel(self,girdi):
        sayı=len(self.data)//500
        yuzdelik=100*100/sayı
        tam=sayı-(girdi//500)
        yıldız=30*100/sayı
            
        print("""\r \t|{}{}| {}  loading ... """.format(
            "#"*int((sayı-tam)*yıldız/100),
            " "*int((tam*yıldız/100)),
            "% "+str(int((sayı-tam)*yuzdelik/100))),
                 )
        
    def veri_duzenle(self):
        
        print("veriler düzenleniyor .. ",end="\n\n")
        time.sleep(2)
        
        for i in range(len(self.data)):
            img=self.siyah_beyaz(self.data[i][0])

            
            self.clear_data.append((img,self.data[i][1]))
            if i%500==0:
                self.gorsel(i)
        
        
            
    def kariştir(self,veri_seti):
        
        for i in tqdm.tqdm(range(0,50,1)):
            shuffle(veri_seti)
        
        print("\n\n")
        return veri_seti
       

    def tuşlara_gore_ayırma(self):
        print("veriler kategorilenip birleştiriliyor ...",end="\n\n")
        time.sleep(2)
        
        for i in tqdm.tqdm(range(0,len(self.clear_data),1)):
            if self.clear_data[i][1]==[1,0,0]:
                self.lefts.append((self.clear_data[i][0],self.clear_data[i][1]))
                
            elif self.clear_data[i][1]==[0,1,0]:
                self.go.append((self.clear_data[i][0],self.clear_data[i][1]))
                
            elif self.clear_data[i][1]==[0,0,1]:
                self.rights.append((self.clear_data[i][0],self.clear_data[i][1]))
        print("\n\n")
        """
            if self.clear_data[i][1]==[1,0,0,0,0,0,0,0]:
                self.lefts.append([self.clear_data[0],self.clear_data[1]])
                
            elif self.clear_data[i][1]==[0,1,0,0,0,0,0,0]:
                self.go.append([self.clear_data[0],self.clear_data[1]])
                
            elif self.clear_data[i][1]==[0,0,1,0,0,0,0,0]:
                self.rights.append([self.clear_data[0],self.clear_data[1]])
                
            elif self.clear_data[i][1]==[0,0,0,1,0,0,0,0]:
                self.rightgo.append([self.clear_data[0],self.clear_data[1]])
                
            elif self.clear_data[i][1]==[0,0,0,0,1,0,0,0]:
                self.leftgo.append([self.clear_data[0],self.clear_data[1]])
                
            elif self.clear_data[i][1]==[0,0,0,0,0,1,0,0]:
                self.arka.append([self.clear_data[0],self.clear_data[1]])
                
            elif self.clear_data[i][1]==[0,0,0,0,0,0,1,0]:
                self.rightarka.append([self.clear_data[0],self.clear_data[1]])
                
            elif self.clear_data[i][1]==[0,0,0,0,0,0,0,1]:
                self.leftarka.append([self.clear_data[0],self.clear_data[1]])
        """
        print("\n\n")
                
    def sonuç(self):
        print("veriler son hale getiriliyor ..",end="\n\n")
        time.sleep(2)
        boyut =self.go[:len(self.lefts)][:len(self.rights)][:len(self.go)]

        print("veriler kariştiriliyor ...",end="\n\n")
        time.sleep(2)
        
        self.lefts=self.kariştir(self.lefts)
        self.rights=self.kariştir(self.rights)
        self.go=self.kariştir(self.go)
        
        self.lefts=self.lefts[:len(boyut)]
        self.rights=self.rights[:len(boyut)]
        self.go=self.go[:len(boyut)]

        

        veri_seti=self.lefts+self.rights+self.go
        veri_seti=self.kariştir(veri_seti)

        print("""
   ______________________________

        self.lefts={}
        self.rights={}
        self.go={}

   ______________________________
        """.format(
        len(self.lefts),
        len(self.rights),
        len(self.go)
        ))
        time.sleep(4)
        print("\n\n")
        return veri_seti

    def kaydet(self,veri_seti):
        """
        for i in veri_seti:
            cv2.imshow("hgklıh",i[0])
            print(i[1])
            if cv2.waitKey(25) & 0xFF==ord("q"):
                cv2.destroyAllWindows()
                break
        """
        print("toplam da işlenebişlecek veri seti : ",len(veri_seti),end="\n\n")
        print("veriler önbelleğe kaydediliyor ...",end="\n\n")
        yol=os.listdir("veri_setleri\\onbellek")

        for i in range(1,1000):
            if f"duzelt_data_{i}.npy" not in yol:
                np.save(f"veri_setleri\\onbellek\\duzelt_data_{i}.npy",veri_seti)
                break
            else:
                pass
        time.sleep(2)
        print(f"duzelt_data_{i}.npy verisi önbelleğe kaydedildi.",end="\n\n")
        print("///////////////////////////////////////////////////",end="\n\n\n")
        
    

        
    
if __name__== "__main__":

    
    yol=os.listdir("veri_setleri")
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
    time.sleep(2)
    for i in range(len(yol)):
        if yol[i].endswith(".npy"):
            veriler=duzenle()
            
            print(f"{yol[i]} veriler cekiliyor .. ",end="\n\n")
            veriler.veri_al(yol[i])

            veriler.veri_duzenle()
            veriler.tuşlara_gore_ayırma()
            veri=veriler.sonuç()
            veriler.kaydet(veri)

            

        else:
            pass


    print("veriler onbellektenl alınıp işleniyor ..",end="\n\n")
    time.sleep(2)
    duzenle=verileri_son_hale_getir.birleştir()

    
        
    
    
