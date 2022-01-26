from cgitb import text
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView


from kivy.uix.button import Button


class WidgetsExample(GridLayout):
	count = 1
	my_text = StringProperty("1")

	def on_button_click(self):
		self.count += 1
		self.my_text = str(self.count)
	
	def on_toggle_button_state(self):
		print('toggle state')
		





class StackLayoutExample(StackLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# self.orientation = "lr-tb"
		for i in range(0, 100):
			b = Button(text="{}".format(i + 1), size_hint=(None, None), size=(dp(100), dp(100)))
			self.add_widget(b)




class AnchorLayoutExample(AnchorLayout):
	pass



# class GridLayoutExample(GridLayout):
# 	pass



class BoxLayoutExample(BoxLayout):
    pass
"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)
"""

class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass 


TheLabApp().run()


