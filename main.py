from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

screen_manager = """
ScreenManager:
    Home:
    Vacation:
    
    
<Home>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Selected one of the following to plan:'
        Button:
            text: 'Plan Future Vacation'
            on_press: root.manager.current = 'vacation'
            size_hint: (.5,.5)
            pos_hint: {'x': .25}
        Button:
            text: 'Plan Rebuild'
            on_press: root.manager.current = 'vacation'
            size_hint: (.5,.5)
            pos_hint: {'x': .25}
            
    
<Vacation>:
    name: 'vacation'
    BoxLayout:
        orientation: 'vertical'
        Button:
            size_hint: (.1,.1)
            pos_hint: {'x': 0, 'top': .1}
            text: '<'
            font_size: 30
            on_press: root.manager.current = 'home'
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'Name of Vacation'
                    size_hint: (.5,.1)
        
                TextInput:
                    id: name
                    size_hint: (.5,.1)
                    
                Label:
                    text: 'How many Weeks/Months do you want to pay for'
                    size_hint: (.5,.1)
                Spinner:
                    id: weeks_months
                    values: 'Week(s)', 'Month(s), Year(s)'
                    size_hint: (.5,.1)
        
                Label:
                    text: 'Name of Vacation'
                    size_hint: (.5,.1)
                TextInput:
                    id: name
                    size_hint: (.5,.1)
               
        
"""


class Home(Screen):
    pass


class Vacation(Screen):
    pass


manage = ScreenManager()
manage.add_widget(Home(name='home'))
manage.add_widget(Vacation(name='vacation'))


class Budget(App):
    salary = NumericProperty()
    total_cost = NumericProperty()
    weeks_months_years = StringProperty()
    length_of_payments = NumericProperty()


    def build(self):
        screen = Builder.load_string(screen_manager)
        return screen


if __name__ == '__main__':
    app = Budget()
    app.run()
