
from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout


class WidgetsExample(GridLayout):
	count = 1
	my_text = StringProperty("answer")
	count_enabled = BooleanProperty(False)
	


	def on_button_click(self):
		if self.count_enabled:
			self.my_text = str(self.count)
	
	def on_toggle_button_state(self, widget):
		if widget.state == "normal":
			widget.text = "show answer"
			self.count_enabled = False
		else:      
			widget.text = "hide answer"
			self.count_enabled = True
	

		

class TheLabApp(App):
    pass 


if __name__ == "__main__":
	TheLabApp().run()


