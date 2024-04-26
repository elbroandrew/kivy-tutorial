
from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout
from sql_conn import Database


class WidgetsExample(GridLayout):
	answer = "text text text text text text text text text"
	my_text = StringProperty("answer")
	
	db = Database()
	db.connect()
	db.create_table()
	db.insert()

	def on_button_click(self, toggle_button):
		self.my_text = ''
		toggle_button.state = "normal"
		res = self.db.fetch_all()
		for r in res:
			print(r)
    
	def on_toggle_button_state(self, widget):
		if widget.state == "normal":
			widget.text = "show answer"
			self.my_text = ''
		else:      
			widget.text = "hide answer"
			self.my_text = self.answer



class TheLabApp(App):
    title = "Exercise app"
    
    def on_stop(self):
        print("QUIT")
    
    
    


if __name__ == "__main__":
	TheLabApp().run()


