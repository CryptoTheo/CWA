from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard


class ResultCard(MDCard):
    place = StringProperty()
    rider_name = StringProperty()
    score = StringProperty()
    difference = StringProperty()
    division = StringProperty(defaultvalue='First Timer')
