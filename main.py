import time
import os
import models
import modeli_test_etme

import veri_seti_duzenle
import verileri_son_hale_getir
import veri_setini_olusturma




class Ana_menu():
    def __init__(self):
        self.anamenu()

    def menu(self):
        print("""
 ________________  SEÇİMİNİ   YAP  ___________________________
|
|
|        [ 1 ]   VERİ OLUŞTUR 
|        -----------------------------
|            [ 2 ]  VERİ DÜZENLE
|        -----------------------------
|        [ 3 ]   MODEL EĞİT 
|        -----------------------------
|            [ 4 ]  MODEL TEST ET
|        -----------------------------
|        [ 5 ]  ÇIKIŞ
|
|_____________________________________________________________
            """)
    def anamenu(self):
        while True:
            self.menu()

            sor = input ("=>> ")

            if sor =="1":
                oluştur=veri_setini_olusturma.veri()
                
            elif sor == "2":
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
                        veriler=veri_seti_duzenle.duzenle()
                        
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



            elif sor == "3":
                model=models.NET()

            elif sor == "4":
                predict=modeli_test_etme.MODEL_NET()

            elif sor == "5" :
                print("çıkılıyor ...")
                time.sleep(2)
                break
            else:
                print("----  HATA TEKRAR DENE -----")
                time.sleep(2)

menu=Ana_menu()
