from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

screen_manager = """
ScreenManager:
    Home:
    Rebuild:
    Vacation:
    Report:
    
    
<Home>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Select one of the following plans:'
        Button:
            text: 'Plan Future Vacation'
            on_press: root.manager.current = 'vacation'
            size_hint: (.5,.5)
            pos_hint: {'x': .25}
        Button:
            text: 'Plan Rebuild'
            on_press: root.manager.current = 'rebuild'
            size_hint: (.5,.5)
            pos_hint: {'x': .25}
            

<Rebuild>:
    name: 'rebuild'
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
                    text: 'Name of (Project)'
                    size_hint: (.5,.1)
        
                TextInput:
                    id: name
                    size_hint: (.5,.1)
                    
                Label:
                    text: 'How many Weeks/Months do you want to pay for'
                    size_hint: (.7,.1)
                Spinner:
                    id: weeks_months
                    values: 'weeks', 'month', 'year'
                    size_hint: (.5,.1)
        
                Label:
                    text: 'For how long'
                    size_hint: (.5,.1)
                TextInput:
                    id: length
                    size_hint: (.5,.1)
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'Your Salary'
                    size_hint: (.5,.1)
        
                TextInput:
                    id: salary
                    size_hint: (.5,.1)
                    
                Label:
                    text: 'Total cost of (Project)'
                    size_hint: (.5,.1)
        
                TextInput:
                    id: total_cost
                    size_hint: (.5,.1)
                    
                Label:
                    text: ''
                    size_hint: (.5,.1)
                
                Button:
                    text: 'Click to Get Report'
                    size_hint: (.5,.1)
                    pos_hint: {'top': .1}
                    on_press: root.update_variables()
                    on_press: root.manager.current = 'report'


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
                    size_hint: (.7,.1)
                Spinner:
                    id: weeks_months
                    values: 'weeks', 'month', 'year'
                    size_hint: (.5,.1)
        
                Label:
                    text: 'For how long'
                    size_hint: (.5,.1)
                TextInput:
                    id: length
                    size_hint: (.5,.1)
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'Your Salary'
                    size_hint: (.5,.1)
        
                TextInput:
                    id: salary
                    size_hint: (.5,.1)
                    
                Label:
                    text: 'Total cost of Vacation'
                    size_hint: (.5,.1)
        
                TextInput:
                    id: total_cost
                    size_hint: (.5,.1)
                    
                Label:
                    text: ''
                    size_hint: (.5,.1)
                
                Button:
                    text: 'Click to Get Report'
                    size_hint: (.5,.1)
                    pos_hint: {'top': .1}
                    on_press: root.get_weekly_payment()
                    on_press: root.get_monthly_payment()
                    on_press: root.yearly_payments()
                    on_press: root.get_salary_percentage()
                    on_press: root.update_variables()
                    on_press: root.manager.current = 'report'
               
        
<Report>:
    name: 'report'
    
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Weekly Payment:'
                size_hint: (.5,.1)
            Label:
                text: app.weekly_payments
                size_hint: (.5,.1)
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Monthly Payment:'
                size_hint: (.5,.1)
            Label:
                text: app.monthly_payments
                size_hint: (.5,.1)
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Yearly Payment:'
                size_hint: (.5,.1)
            Label:
                text: app.yearly_payments
                size_hint: (.5,.1)
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Percentage of Salary:'
                size_hint: (.5,.1)
            Label:
                text: app.salary_percentage
                size_hint: (.5,.1)
    
    
"""


class Home(Screen):
    pass


class Rebuild(Screen):
    def update_variables(self):
        app.salary = int(self.ids.salary.text)
        app.total_cost = int(self.ids.total_cost.text)
        app.weeks_months_years = self.ids.weeks_months.text
        app.length_of_payments = int(self.ids.length.text)

    def get_days(self):
        if app.weeks_months_years == 'weeks':
            return app.length_of_payments * 7
        elif app.weeks_months_years == 'months':
            return app.length_of_payments * 30
        elif app.weeks_months_years == 'years':
            return app.length_of_payments * 365.25

    def get_weekly_payment(self):
        app.weekly_payments = str(app.total_cost / (self.get_days() / 7))

    def get_monthly_payment(self):
        app.monthly_payments = str(app.total_cost / (self.get_days() / 30))

    def yearly_payments(self):
        app.yearly_payments = str(app.total_cost / (self.get_days() / 30))

    def get_salary_percentage(self):
        app.salary_percentage = str(app.total_cost / app.salary)


class Vacation(Screen):
    def update_variables(self):
        app.salary = int(self.ids.salary.text)
        app.total_cost = int(self.ids.total_cost.text)
        app.weeks_months_years = self.ids.weeks_months.text
        app.length_of_payments = int(self.ids.length.text)

    def get_days(self):
        if app.weeks_months_years == 'weeks':
            return app.length_of_payments * 7
        elif app.weeks_months_years == 'months':
            return app.length_of_payments * 30
        elif app.weeks_months_years == 'years':
            return app.length_of_payments * 365.25

    def get_weekly_payment(self):
        app.weekly_payments = str(app.total_cost / (self.get_days() / 7))

    def get_monthly_payment(self):
        app.monthly_payments = str(app.total_cost / (self.get_days() / 30))

    def yearly_payments(self):
        app.yearly_payments = str(app.total_cost / (self.get_days() / 30))

    def get_salary_percentage(self):
        app.salary_percentage = str(app.total_cost / app.salary)


class Report(Screen):
    pass


manage = ScreenManager()
manage.add_widget(Home(name='home'))
manage.add_widget(Rebuild(name='rebuild'))
manage.add_widget(Vacation(name='vacation'))
manage.add_widget(Report(name='report'))


class Budget(App):
    salary = NumericProperty()
    total_cost = NumericProperty()
    weeks_months_years = StringProperty()
    length_of_payments = NumericProperty()
    weekly_payments = StringProperty()
    monthly_payments = StringProperty()
    yearly_payments = StringProperty()
    salary_percentage = StringProperty()


    def build(self):
        screen = Builder.load_string(screen_manager)
        return screen


if __name__ == '__main__':
    app = Budget()
    app.run()
