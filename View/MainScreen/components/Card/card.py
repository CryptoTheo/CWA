from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard



class NavCard(MDCard):
    image = StringProperty()
    label = StringProperty()
    tag = StringProperty()
    screen = StringProperty()

    # def __init__(self):
    #     super(NavCard, self).__init__()()
    #     elevation = dp(2)
