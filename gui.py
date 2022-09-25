import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from kivy.uix.filechooser import FileChooserListView

from src.action import Action

Window.size = (450, 300)
sm = ScreenManager()
screens = []
action = Action()

def go_home(e):
    sm.switch_to(screens[0])

class BRUTEFORCEFTP(Screen):
    values = None
    chooser = None
    def __init__(self, **kwargs):
        super(BRUTEFORCEFTP, self).__init__(**kwargs)
        grid = GridLayout(cols=1, spacing=[1, 3], padding=[10, 10])
        inputs = BoxLayout()
        self.host = TextInput(text='192.168.43.1', multiline=False)
        self.port = TextInput(text='21', multiline=False)
        self.user = TextInput(text='admin', multiline=False)
        inputs.add_widget(self.host)
        inputs.add_widget(self.port)
        inputs.add_widget(self.user)
        grid.add_widget(inputs)

        action = BoxLayout()
        def add(instance):
            if self.chooser:
                box_file.remove_widget(self.chooser)
                self.chooser = None
                return
            self.chooser = FileChooserListView(
                filters=[
                    lambda folder, filename: not filename.endswith('.sys')
                ]
            )
            self.chooser.bind(selection=self.ask_file)
            box_file.add_widget(self.chooser)

        box_file = BoxLayout(size_hint=(1, None), height=160)
        menu = BoxLayout()
        menu.add_widget(Button(
            text='Select Password List',
            size_hint=(0.4, None),
            height=30,
            on_press=add
        ))
        grid.add_widget(box_file)
        grid.add_widget(menu)
        action.add_widget(Button(
            text='Start',
            background_color= '#1565C0',
            size_hint=(0.4, None),
            height=30,
            on_press=self.start
        ))
        action.add_widget(Button(
            text='Back',
            size_hint=(0.4, None),
            height=30,
            on_press=go_home,
            background_color='red'
        ))
        grid.add_widget(action)
        self.add_widget(grid)
    def start(self, instance):
        if self.values:
            action.bruteforce_ftp(self.host.text, self.user.text, self.values, self.port.text)
        else:
            action.bruteforce_ftp(self.host.text, self.user.text, None, self.port.text)

    def ask_file(self, instance, value):
        if len(value):
            self.values = value[0]

class BRUTEFORCEFB(Screen):
    chooser = None
    values = None
    def __init__(self, **kwargs):
        super(BRUTEFORCEFB, self).__init__(**kwargs)
        grid = GridLayout(cols=1, spacing=[1, 3], padding=[10, 10])
        stack = StackLayout()
        self.email = TextInput(multiline=False, text='@mail.com', size_hint=(None, 1.3), width=215)
        self.manual = TextInput(multiline=False, text='password (Optional)', size_hint=(None, 1.3), width=215)
        stack.add_widget(self.email)
        stack.add_widget(self.manual)
        grid.add_widget(stack)

        action = BoxLayout()
        def add(instance):
            if self.chooser:
                box_file.remove_widget(self.chooser)
                self.chooser = None
                return

            self.chooser = FileChooserListView(
                filters=[
                    lambda folder, filename: not filename.endswith('.sys')
                ]
            )
            self.chooser.bind(selection=self.ask_file)
            box_file.add_widget(self.chooser)

        box_file = BoxLayout(size_hint=(1, None), height=200)
        menu = BoxLayout()
        menu.add_widget(Button(
            text='Select Password List',
            size_hint=(0.4, None),
            height=25,
            on_press=add
        ))
        grid.add_widget(box_file)
        grid.add_widget(menu)
        action.add_widget(Button(
            text='Start',
            background_color= '#1565C0',
            size_hint=(0.4, None),
            height=30,
            on_press=self.start
        ))
        action.add_widget(Button(
            text='Back',
            size_hint=(0.4, None),
            height=30,
            on_press=go_home,
            background_color='red'
        ))
        grid.add_widget(action)
        self.add_widget(grid)
    def start(self, instance):
        if self.email != '@mail.com':
            if self.manual.text != 'password (Optional)':
                return action.bruteforce_fb(self.email.text, self.manual.text)
            if self.values:
                return action.bruteforce_fb(self.email.text, None, self.values)
            else:
                action.bruteforce_fb(self.email.text)

    def ask_file(self, instance, value):
        if len(value):
            self.values = value[0]

class BRUTEFORCEZIP(Screen):
    active_chooser = ''
    values = dict()
    chooser = None
    def __init__(self, **kwargs):
        super(BRUTEFORCEZIP, self).__init__(**kwargs)
        grid = GridLayout(cols=1, spacing=[1, 3], padding=[10, 10])
        action = BoxLayout()
        def add(instance):
            self.active_chooser = instance.text
            if self.chooser:
                return
            self.chooser = FileChooserListView(
                filters=[
                    lambda folder, filename: not filename.endswith('.sys')
                ]
            )
            self.chooser.bind(selection=self.ask_file)
            box_file.add_widget(self.chooser)

        box_file = BoxLayout(size_hint=(1, None), height=200)
        menu = BoxLayout()
        menu.add_widget(Button(
            text='Select ZIP',
            size_hint=(0.4, None),
            height=30,
            on_press=add
        ))
        menu.add_widget(Button(
            text='Select Password List',
            size_hint=(0.4, None),
            height=30,
            on_press=add
        ))
        grid.add_widget(box_file)
        grid.add_widget(menu)
        action.add_widget(Button(
            text='Start',
            background_color= '#1565C0',
            size_hint=(0.4, None),
            height=30,
            on_press=self.start
        ))
        action.add_widget(Button(
            text='Back',
            size_hint=(0.4, None),
            height=30,
            on_press=go_home,
            background_color='red'
        ))
        grid.add_widget(action)
        self.add_widget(grid)
    def start(self, instance):
        if 'Select ZIP' in self.values and 'Select Password List' in self.values:
            action.bruteforce_zip(self.values['Select ZIP'], self.values['Select Password List'])
        elif self.values['Select ZIP']:
            action.bruteforce_zip(self.values['Select ZIP'], None)

    def ask_file(self, instance, value):
        if len(value):
            self.values[self.active_chooser] = value[0]

class REQUEST(Screen):
    def __init__(self, **kwargs):
        super(REQUEST, self).__init__(**kwargs)
        grid = GridLayout(cols=2, spacing=[1, 3], padding=[10, 10])
        label = Label(
            text='URL',
            halign="left",
            valign= 'middle',
            size_hint=(None, 0.2),
            width=100
        )
        label.text_size = label.size
        grid.add_widget(label)
        self.url = TextInput(
            text='https://',
            size_hint=(None, 0.5),
            multiline=False,
            width=250
        )
        grid.add_widget(self.url)

        label = Label(
            text='Data',
            halign="left",
            valign= 'middle',
            size_hint=(None, 0.2),
        )
        label.text_size = label.size
        grid.add_widget(label)

        self.data = TextInput(
            text= "{}",
            size_hint=(None, 1),
            multiline=True,
            width=250
        )
        grid.add_widget(self.data)

        label = Label(
            text='Header',
            size_hint=(None, 0.2),
            halign="left",
            valign= 'middle'
        )
        label.text_size = label.size
        grid.add_widget(label)

        self.header = TextInput(
            text= "{}",
            size_hint=(None, 1),
            multiline=True,
            width=250
        )
        grid.add_widget(self.header)

        def callback(instance, value):
            print(value, instance.active)
            if value:
                pass
            else:
                pass

        box = BoxLayout(width=250)
        label = Label(
            text='Methods',
            size_hint=(None, 0.2),
            halign="left",
            valign= 'middle'
        )
        label.text_size = label.size
        grid.add_widget(label)

        # checkbox.bind(active=callback)
        checkbox = CheckBox(group='methods')
        checkbox_2 = CheckBox(group='methods')
        checkbox_3 = CheckBox(group='methods')
        checkbox_4 = CheckBox(group='methods')
        self.checkbox = [checkbox, checkbox_2, checkbox_3, checkbox_4]
        
        box.add_widget(checkbox)
        box.add_widget(Label(
            text='Get',
            font_size='12sp'
        ))
        box.add_widget(checkbox_2)
        box.add_widget(Label(
            text='Post',
            font_size='12sp'
        ))
        box.add_widget(checkbox_3)
        box.add_widget(Label(
            text='Delete',
            font_size='12sp'
        ))
        box.add_widget(checkbox_4)
        box.add_widget(Label(
            text='Put',
            font_size='12sp'
        ))

        grid.add_widget(box)

        action = BoxLayout()
        action.add_widget(Button(
            text='Start',
            background_color= '#1565C0',
            size_hint=(None, 0.5),
            on_press=self.start
        ))
        action.add_widget(Button(
            text='Back',
            size_hint=(None, 0.5),
            on_press=go_home,
            background_color='red'
        ))
        grid.add_widget(action)
        self.add_widget(grid)
    def start(self, instance):
        method = "get"
        data = None
        header = None
        if self.checkbox[0].active:
            method = 'get'
        if self.checkbox[1].active:
            method = 'post'
        if self.checkbox[2].active:
            method = 'put'
        if self.checkbox[3].active:
            method = 'delete'
        if self.data.text != '{}':
            data = self.data.text
        if self.header.text != '{}':
            header = self.header.text

        action.request(self.url.text, method, data, header)

class DDOS(Screen):
    def __init__(self, **kwargs):
        super(DDOS, self).__init__(**kwargs)
        grid = GridLayout(cols=1, spacing=[1, 3], padding=[10, 10])
        grid.add_widget(Label(
            text='IP Address',
            size_hint=(0.4, 0.2)
        ))
        self.ip = TextInput(
            text='127.0.0.1',
            size_hint=(0.4, 0.5),
            multiline=False
        )
        grid.add_widget(self.ip)
        grid.add_widget(Label(
            text='Port (Optional)',
            size_hint=(0.4, 0.2)
        ))
        self.port = TextInput(
            text='0',
            size_hint=(0.4, 0.5),
            multiline=False
        )
        grid.add_widget(self.port)
        action = BoxLayout()
        action.add_widget(Button(
            text='Start',
            background_color= '#1565C0',
            size_hint=(0.4, 0.3),
            on_press=self.start
        ))
        action.add_widget(Button(
            text='Back',
            size_hint=(0.4, 0.3),
            on_press=go_home,
            background_color='red'
        ))
        grid.add_widget(action)
        self.add_widget(grid)
    def start(self, instance):
        action.ddos(self.ip.text, self.port.text)

class IPPORT(Screen):
    def __init__(self, **kwargs):
        super(IPPORT, self).__init__(**kwargs)
        grid = GridLayout(cols=1, spacing=[1, 3], padding=[10, 10])
        grid.add_widget(Label(
            text='IP Address',
            size_hint=(0.4, 0.2)
        ))
        self.ip = TextInput(
            text='127.0.0.1',
            size_hint=(0.4, 0.5),
            multiline=False
        )
        grid.add_widget(self.ip)
        grid.add_widget(Label(text=''))
        action = BoxLayout()
        action.add_widget(Button(
            text='Start',
            background_color= '#1565C0',
            size_hint=(0.4, 0.3),
            on_press=self.start
        ))
        action.add_widget(Button(
            text='Back',
            size_hint=(0.4, 0.3),
            on_press=go_home,
            background_color='red'
        ))
        grid.add_widget(action)
        self.add_widget(grid)
    def start(self, instance):
        action.ip_port(self.ip.text)

class IPCHECK(Screen):
    def __init__(self, **kwargs):
        super(IPCHECK, self).__init__(**kwargs)
        grid = GridLayout(cols=1, spacing=[1, 3], padding=[10, 10])
        grid.add_widget(Label(
            text='Hostname',
            size_hint=(0.4, 0.2)
        ))
        self.hostname = TextInput(
            text='google.com',
            size_hint=(0.4, 0.5),
            multiline=False
        )
        grid.add_widget(self.hostname)
        grid.add_widget(Label(text=''))
        action = BoxLayout()
        action.add_widget(Button(
            text='Start',
            background_color= '#1565C0',
            size_hint=(0.4, 0.3),
            on_press=self.start
        ))
        action.add_widget(Button(
            text='Back',
            size_hint=(0.4, 0.3),
            on_press=go_home,
            background_color='red'
        ))
        grid.add_widget(action)
        self.add_widget(grid)
    def start(self, instance):
        action.ip_check(self.hostname.text)

class HOME(Screen):
    Bool = BooleanProperty(value=False)
    def __init__(self, **kwargs):
        super(HOME, self).__init__(**kwargs)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        box = BoxLayout(padding=[10, 10])
        left = AnchorLayout(anchor_x='left', anchor_y='top')
        left_21 = BoxLayout(size_hint=(1, 1), orientation='vertical')
        listing = [
            ("Bruteforce Facebook"),
            ("Bruteforce ZIP"),
            ("Bruteforce FTP"),
            ("DDOS"),
            ("IP Check"),
            ("IP Port"),
            ("Request"),
        ]
        for i in listing:
            left_21.add_widget(Button(
                text=i,
                size_hint= (1, .2),
                font_size= 11,
                background_color= '#1565C0',
                on_press=self.click
            ))

        left.add_widget(left_21)
        box.add_widget(left)
        root.add_widget(box)
        self.add_widget(root)

    def click(self, a):
        global screens

        if a.text == 'DDOS':
            sm.switch_to(screens[1])
        if a.text == 'IP Port':
            sm.switch_to(screens[2])
        if a.text == 'IP Check':
            sm.switch_to(screens[3])
        if a.text == 'Request':
            sm.switch_to(screens[4])
        if a.text == 'Bruteforce ZIP':
            sm.switch_to(screens[5])
        if a.text == 'Bruteforce Facebook':
            sm.switch_to(screens[6])
        if a.text == 'Bruteforce FTP':
            sm.switch_to(screens[7])

class HackByFerdiansyah0611(App):
    def build(self):
        global screens
        screens = [
            HOME(name='home'),
            DDOS(name='ddos'),
            IPPORT(name='ipport'),
            IPCHECK(name='ipcheck'),
            REQUEST(name='request'),
            BRUTEFORCEZIP(name='bruteforcezip'),
            BRUTEFORCEFB(name='bruteforcefb'),
            BRUTEFORCEFTP(name='bruteforceftp'),
        ]
        for i in screens:
            sm.add_widget(i)
        return sm

if __name__ == '__main__':
    HackByFerdiansyah0611().run() 