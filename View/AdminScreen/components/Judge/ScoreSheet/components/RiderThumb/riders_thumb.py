from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivy.uix.popup import Popup
from kivymd.uix.card import MDCard


class RidersThumb(MDCard):
    # image = ObjectProperty()
    # rider_age = StringProperty()
    rider_name = StringProperty()
    rider_stance = StringProperty()
    bib_color = StringProperty()
    rider_id = StringProperty()
    contest_id = StringProperty()
    # section = StringProperty()

    def on_release(self):
        pass
