
from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout
from sql_conn import Database


class WidgetsExample(GridLayout):
	answer = "text text text text text text text text text"
	my_text = StringProperty("answer")
	
	with Database() as db:
		db.create_table()
		db.insert()
		res = db.fetch_all()
		for r in res:
			print(r)

	

	def on_button_click(self, toggle_button):
		self.my_text = ''
		toggle_button.state = "normal"
    
	def on_toggle_button_state(self, widget):
		if widget.state == "normal":
			widget.text = "show answer"
			self.my_text = ''
		else:      
			widget.text = "hide answer"
			self.my_text = self.answer



class TheLabApp(App):
    title = "Exercise app"
    
    
    


if __name__ == "__main__":
	TheLabApp().run()


