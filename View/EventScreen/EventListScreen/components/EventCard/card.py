from kivy.properties import StringProperty
from kivymd.uix.card import MDCard


class EventCard(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.elevation = 2.5

    event_name = StringProperty()
    event_description = StringProperty()
    event_format = StringProperty()
    event_date = StringProperty()
    event_location = StringProperty()
    # event_photo = StringProperty()
    event_uid = StringProperty()
