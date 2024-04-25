
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image 
from kivy.uix.label import Label
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.core.window import Window

class GridLayoutExample(GridLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 5
        self.row_force_default=True
        self.row_default_height=100
         
        hello = Label(text="Hello", font_size='20sp')
        hello.color = (0.5, 0.7, 0.6)
        self.add_widget(hello)
        
        b1 = Button(text="A", width=100, height=100)
        self.add_widget(b1)
        b2 = Button(text="A", width=100, height=100)
        self.add_widget(b2)
    




class TheLab2App(App):
    def build(self):
        
        self.root = root = GridLayoutExample()
        self.root.bind(size=self._update_rect, pos=self._update_rect)
        
        # self.window.add_widget(Image(source="images/lab_logo.png"))
       
        
        with root.canvas.before:
            Color(0.5, 0.4, 0.2, 1)  # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
            return root
        
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
        


if __name__ == "__main__":
    TheLab2App().run()