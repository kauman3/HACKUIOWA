from kivy.app import App
from kivy.lang import Builder
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
    
"""


class Home(Screen):
    pass


class Vacation(Screen):
    pass


manage = ScreenManager()
manage.add_widget(Home(name='home'))
manage.add_widget(Vacation(name='vacation'))


class Budget(App):
    def build(self):
        screen = Builder.load_string(screen_manager)
        return screen


if __name__ == '__main__':
    app = Budget()
    app.run()
