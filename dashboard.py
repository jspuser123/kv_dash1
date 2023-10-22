from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

#from kivymd.uix.textfield import MDTextField
#from kivymd.uix.button import MDRoundFlatButton,MDFlatButton
#from kivymd.icon_definitions import md_icons
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
#import kivymd_extensions.akivymd
from matplotlib import pyplot as plt
#from kivy.garden.matplotlib import FigureCanvasKivyAgg
#import Label kivy.core.text.Label 
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import numpy as np
from kivy.core.window import Window

#Window.size=(1280,780)

#Config.set('graphics', 'resizeble', 'True')

#Config.write()

Builder.load_string(
'''
<login>:
   FloatLayout:
      canvas.before:
         Rectangle:
            pos: self.pos
            size: self.size
            source: 'im.jpg'
      MDRoundFlatButton:
         text: "menu"
         font_size: 20
         pos_hint: {"center_x": 0.5,"center_y":.5}
            #text_color: 5, 5, 5, 5
            #md_bg_color: 3, 3, 3, 3
         on_press:
            app.root.current = 'sucess'
            app.root.transition.direction = 'left'
            

<loginck>:
  
     
   MDBoxLayout:
      size_hint_y:.04
      md_bg_color: 0,0,2,3
   
      MDLabel:
         text: "Create an dashboard"
         font_size: 20
         pos_hint_x:.7
         theme_text_color: "Custom"
         text_color: "pink"
         #pos_hint: {"center_x":.5,"center_y":.1}
      MDLabel:
         text: "power of by jagan create www.js.com"
         font_size: 20
         pos_hint_x:.9
         theme_text_color: "Custom"
         text_color: "white"
         #pos_hint: {"center_x":.5,"center_y":.1}
      
   MDBoxLayout:
      md_bg_color:"blue"
      size_hint: 1,.2
      pos_hint: {"top":1}
      
      
      
      MDTextField:
         id: search
         size_hint: .3,None
         pos_hint: {"top":1,}
         #pos_hint: {"center_x": .60,"center_y":.98}
         #pos:600,900
         icon_left: "magnify"
         mode: "round"
         hint_text: "enter google search"
      MDIconButton:
         icon: "account"
         
         
         pos_hint: {"top":1, "center_x": .86}

      MDIconButton:
         icon: "email"
         pos_hint: {"center_x": .89, "top":1}
      MDIconButton:
         icon: "camera-iris"
         pos_hint: {"center_x": .92, "top":1}
      MDIconButton:
         icon: "comment-multiple"
         pos_hint: {"center_x": .95, "top":1,}
      
      MDIconButton:
         icon: "cog-outline"
         pos_hint: {"center_x": .98, "top":1,}



                     
   
     
   MDBoxLayout:
      id:bo
      md_bg_color: 0,33,3,1
      radius: [0, 0, 25, 25]
      size_hint_x:.15
     
      
      ScrollView:
         md_bg_color:"blue"
         
         MDList:
            id: container
            #md_bg_color: 2,2,2,5
            
            OneLineAvatarListItem:
               id:lis
               #md_bg_color: 0,0,23,5
               text: "menu"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "user"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "email"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "password"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "name"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "data_list"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "arun"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "jagan list"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "amount"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "bank detalis"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "jagan list"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "jagan list"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "jagan list"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "jagan list"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "jagan list"
               ImageLeftWidget:
                  source: "im2.jpeg"
            OneLineAvatarListItem:
               id:lis
               text: "jagan list"
               ImageLeftWidget:
                  source: "im2.jpeg"
               
            OneLineAvatarListItem:
               id:lis
               text: "jagan list"
               ImageLeftWidget:
                  source: "im2.jpeg"
##########
   BoxLayout:
      orientation:"vertical"
    
      size_hint:.85,.8
      pos_hint: {"x":.15,"y":.05}


      MDCard:
         
         spacing:"10dp"
         paddiing:"10dp"

         MDCard:
            md_bg_color:"pink"
            
            MDRelativeLayout:
            
                  
            
            
                  

               Label:
                  text:'Control Process'
                  color:0,0,2,1
                  pos_hint: {"center_x": 0.2,"center_y":.88}
                  size_hint:None,None
                  width:100
                  hight:100


               Label:
                  text:'cpu'
                  color:0,0,2,1
                  pos_hint: {"center_x": 0.2,"center_y":.74}
                  size_hint:None,None
                  width:100
                  hight:100

               Label:
                  text:'ram'
                  color:0,0,2,1
                  pos_hint: {"center_x": 0.35,"center_y":.74}
                  size_hint:None,None
                  width:100
                  hight:100

               Label:
                  id:circle_process
                  text:'100%'
                  color:0,0,2,1
                  pos_hint: {"x": .1,"center_y":.5}
                  size_hint:None,None
                  width:100
                  hight:100
                  
                  canvas.before:
                     Color:
                        rgba: 0, 0, 1, 1
                     Ellipse:
                        size:self.size
                        pos:self.pos
                  
                     Ellipse:
                        size:self.size
                        pos:self.pos
                        angle_end:100
                  
                     Color:
                        rgba: 1, 1, 0, 1
                     Ellipse:
                        size:[self.width - 30,self.width -30]
                        pos:[(self.center_x - (self.width - 30)/2),(self.center_y -(self.hight - 30)/2)]

               Label:
                  id:circle_process1
                  text:'50%'
                  color:0,0,2,1
                  pos_hint: {"x": .35,"center_y":.5}
                  size_hint:None,None
                  width:100
                  hight:100
                  
                  canvas.before:
                     Color:
                        rgba: 0, 0, 1, 1
                     Ellipse:
                        size:self.size
                        pos:self.pos
                  
                     Color:
                        rgba: 0, 1, 1, 1
                     Ellipse:
                        size:self.size
                        pos:self.pos
                        angle_end:50
                  
                     Color:
                        rgba: 1, 1, 0, 1
                     Ellipse:
                        size:[self.width - 30,self.width -30]
                        pos:[(self.center_x - (self.width - 30)/2),(self.center_y -(self.hight - 30)/2)]
         MDCard:
            md_bg_color:"blue"
            id:bar
         MDCard:
            md_bg_color:"grey"
            id:pie
      MDCard:
         spacing:"5dp"
         padding:"5dp"


        
         MDCard:
            md_bg_color:"red"
            id:wave
         MDCard:
            md_bg_color:"pink"
            id:table

         
         
   
  
      

''')

class login(Screen):
      pass


class loginck(Screen):
      def __init__(self, **kwargs):
          super().__init__(**kwargs)
          
          data_tables = MDDataTable(
            pos_hint={"center_x":.5, "center_y": .5},
                
            
            use_pagination=True,
            column_data=[
                ("No.", dp(30)),
                ("Column 1", dp(30)),
                ("Column 2", dp(30)),
                ("Column 3", dp(30)),
                ("Column 4", dp(30)),
                ("Column 5", dp(30)),
                ],
            row_data=[
                (f"{i + 1}", "1", "2", "3", "4", "5") for i in range(50)
                ],
            )
          self.ids.table.add_widget(data_tables)
         
         
      # bar   #######################
          
          x = np.array(["A", "B", "c", "D"])
          x5= np.array(["x","y","z","m"])
          y = np.array([3, 8, 1, 10])

          fig = plt.figure()
          fig = plt.bar(x,y,color="hotpink")
          fig = plt.bar (x5,y,color="purple")
          fig=plt.ylabel("This is MY Y Axis")
          fig=plt.xlabel("This is my X Axis")
          self.ids.bar.add_widget(FigureCanvasKivyAgg(plt.gcf()))
          #############################
          
        
       #wave
          l3 = FloatLayout()
          x = np.linspace(0, 20, 201)
          y = np.sin(x)
          fig1 = plt.figure(figsize = (5, 5))
          fig1=plt.plot(x, y, 'b')
          fig1=plt.ylabel("This is MY Y Axis")
          fig1=plt.xlabel("This is X Axis")
          self.ids.wave.add_widget(FigureCanvasKivyAgg(plt.gcf()))
          
          
          
          ###########################
      #round
          l4 = FloatLayout()
          y3 = np.array([35, 25, 25, 15])
          
          fig2 = plt.figure()
          fig2 =  plt.pie(y3)
          fig2=plt.ylabel("This is MY Y Axis")
          fig2=plt.xlabel("X Axis")
          self.ids.pie.add_widget(FigureCanvasKivyAgg(plt.gcf()))
          
        
          
      #grap
           #l3 = FloatLayout()
          #x1 = [1,2,3,4,5]
          #y1 = [5, 12, 6, 9, 15]
          #fig1 = plt.figure()
          #fig1 = plt.plot(x1,y1)
          #fig1=plt.ylabel("This is MY Y Axis")
          #fig1=plt.xlabel("This is X Axis")
          #l3.add_widget(FigureCanvasKivyAgg(plt.gcf(),pos_hint={"center_x":.84, "center_y": .65},size_hint=(.3,.4)))
          #self.add_widget(l3)
          
          
          
         
          
          
          
         
         
         
         
         


sm = ScreenManager()

class TestApp(MDApp):

    def build(self):
        sm.add_widget(login(name='menu'))
        sm.add_widget(loginck(name='sucess'))

        return sm



TestApp().run()

