import time
import sys    
class kumanda():
    def __init__(self,tv_durumu = "Kapalı",tv_ses = 0,anlik_kanal = "TRT",kanal_listesi = ["TRT","Kanal D","Atv"]):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.anlik_kanal = anlik_kanal
        self.kanal_listesi = kanal_listesi
    def tv_ackapa(self):
        if self.tv_durumu == "Kapalı":
            print("Televizyon Açılıyor")
            time.sleep(1)
            self.tv_durumu = "Açık"
            print("Televizyon Açıldı")
            return True
        elif self.tv_durumu == "Açık":
            print("Televizyon Kapatılıyor...")
            time.sleep(1)
            self.tv_durumu = "Kapalı"
            print("Televizyon Kapandı.")
            time.sleep(2)
            sys.exit()
            return False
    def ses_arttir(self):
        if self.tv_durumu == "Açık":
            if self.tv_ses < 32:
                self.tv_ses += 2
                print(self.tv_ses)
            elif self.tv_ses == 32:
                print("Ses Maksimum Seviyede")
        else:
            print("Televizyon Kapalı")
    def ses_azalt(self):
        if self.tv_durumu == "Açık":
            if self.tv_ses > 0:
                self.tv_ses -= 2
                print(self.tv_ses)
            elif self.tv_ses == 0:
                print("Ses Minimum Seviyede")
        else:
            print("Televizyon Kapalı")
    def kanal_ilerlet(self):
        if self.tv_durumu == "Açık": 
            try:
                index = self.kanal_listesi.index(self.anlik_kanal)
                self.anlik_kanal = self.kanal_listesi[index+1]
                print("Şu anki kanal \n>>> {}".format(self.anlik_kanal))
            except(IndexError):
                self.anlik_kanal = self.kanal_listesi[0]
        else:
            print("Televizyon Kapalı")
    def kanal_gerilet(self):
        if self.tv_durumu == "Açık":
            try:
                index = self.kanal_listesi.index(self.anlik_kanal)
                self.anlik_kanal = self.kanal_listesi[index-1]
                print("Şu anki kanal \n>>> {}".format(self.anlik_kanal))
            except(IndexError):
                self.anlik_kanal = self.kanal_listesi[0]
        else:
            print("Televizyon Kapalı")
    def kanal_listele(self):
        if self.tv_durumu == "Açık":
            print(100*"-")
            for x in self.kanal_listesi:
                print(">>>" + x)
            print(100*"-")
        else:
            print("Televizyon Kapalı")
    def kanal_ekle(self):
        kanal_adi = input("Kanal Adını Giriniz :")
        print("Kanal Ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(">>>"+ kanal_adi)
        print("Kanal Eklendi.")
    def kanal_sil(self,kanal_adi):
        self.kanal_listesi.remove(kanal_adi)
    def suanki_kanal(self):
        print("Şu anki Kanal :\n{}".format(self.anlik_kanal))
