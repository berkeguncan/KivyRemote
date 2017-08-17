import kivy
kivy.require("1.10.0")
from kivy.lang import Builder
Builder.load_file("mainkvm.kv")
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.modalview import ModalView
from kumanda import kumanda
import time
import sys   
class Taban(BoxLayout):
    pass
class silisim(ModalView):
    pass
class Uygulamam(App):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.kumanda = kumanda()
    def build(self):
        return Taban() 
    def showSil(self):
        m = silisim()
        m.open()
    def sil(self):
        kanal_adi=str(silisim.ids["delete"].text)
        self.kumanda.kanal_sil(kanal_adi)
        print("Silindi")
if __name__ == "__main__":
    Window.clearcolor = (0,1,1,0)
    Window.size = 300,700
    Uygulamam().run()
