import kivy
kivy.require("1.10.0")
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.modalview import ModalView
from kumanda import kumanda
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition
import time
import sys

class silisim(Screen):
    pass   
class Taban(Screen):
    pass
class Ekranci(ScreenManager):
    pass

sunum = Builder.load_file("mainkvm.kv")

class Uygulamam(App):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.kumanda = kumanda()
    def build(self):
        return sunum 
    def sil(self):
        kanal_adi = silisim.root.ids["delete"].text
        self.kumanda.kanal_sil(kanal_adi)
        print("Silindi")
if __name__ == "__main__":
    Window.clearcolor = (0,1,1,0)
    Window.size = 300,700
    Uygulamam().run()
