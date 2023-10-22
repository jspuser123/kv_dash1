from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import os


k=(
'''
MDScreen:
    MDBoxLayout:
        orientation:"vertical"
        pos_hint: {"x":.1,"y":.1}
        size_hint:.8,.8
        md_bg_color:"pink"
        MDRoundFlatButton:
            pos_hint: {"x":.5}
            text:"hai"
            on_press:app.t1()

    
''')
class Ts():
    def t2(self):
        print('hi')
#sm = ScreenManager()

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(k)
    def t1(self):
        os.system('uname -a')
        print("hai")



TestApp().run()