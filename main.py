
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from sql_conn import Database
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button


class WidgetsExample(GridLayout):
    answer = "text text text text text text text text text"
    my_text = StringProperty("answer")
    app = None
    
    def on_button_click(self, toggle_button):
        self.my_text = ''
        toggle_button.state = "normal"
        self.app = App.get_running_app()
        print("MY APP: ", App.get_running_app())
        res = self.app.db.fetch_all()
        for r in res:
            print(r)
    
    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "show answer"
            self.my_text = ''
        else:      
            widget.text = "hide answer"
            self.my_text = self.answer
            
    def on_text_validate(self, widget):
        '''saves text definition to DB'''
        pass
    
    def on_add_button_click(self):
        pass


class TheLabApp(App):
    title = "Practice collocations"
    
    def on_start(self):
        self.db = Database()
        self.db.connect()
        self.db.create_table()
        self.db.insert()
    
    def on_stop(self):
        self.db.close()
        print("QUIT")
    
    
    


if __name__ == "__main__":
	TheLabApp().run()


