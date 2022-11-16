from kivy.animation import Animation
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.chip import MDChip
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.snackbar import Snackbar

from database import Rider


class RidersAdmin(MDCard):
    filename = StringProperty()
    url = StringProperty()

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_date_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        # Todo change dob to readable script
        self.ids.DOB.text = str(value)
        # print(instance, value, date_range)
        # print((value))

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_image(self):
        url = self.ids.image_link.text
        print(url)
        print(type(url))
        # img = AsyncImage(source=url)
        self.ids.profile_image.source = url

    def add_rider(self):
        rider = Rider()
        rider.first_name = self.ids.first.text
        rider.stance = self.ids.stance.text
        rider.last_name = self.ids.last.text
        # rider.email = self.ids.email.text
        rider.date_of_birth = self.ids.DOB.text
        rider.athlete = self.ids.athlete.active
        rider.judge = self.ids.judge.active
        rider.admin = self.ids.admin.active
        # rider.image = self.ids.image_link.text  #TODO PHASE 2: change from default to take photo
        rider.save()
        self.clear_form()
        Snackbar(text='Rider Added Successfully').open()

    def clear_form(self):
        self.ids.first.text = ''
        self.ids.last.text = ''
        # self.ids.email.text = ''
        self.ids.stance.text = ''
        self.ids.DOB.text = 'Date of Birth'
        # self.ids.image_link.text = ''
        # self.ids.rider.active = True
        # self.ids.judge.active = False
        # self.ids.admin.active = False


class MyChip(MDChip):
    icon_check_color = (0, 0, 0, 1)
    text_color = (0, 0, 0, 0.5)
    _no_ripple_effect = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(active=self.set_chip_bg_color)
        # self.bind(active=self.set_chip_text_color)

    def set_chip_bg_color(self, instance_chip, active_value: int):
        '''
        Will be called every time the chip is activated/deactivated.
        Sets the background color of the chip.
        '''

        self.md_bg_color = (
            (0, 0, 0, 0.4)
            if active_value
            else (
                self.theme_cls.bg_darkest
                if self.theme_cls.theme_style == "Light"
                else (
                    self.theme_cls.bg_light
                    if not self.disabled
                    else self.theme_cls.disabled_hint_text_color
                )
            )
        )

        def set_chip_text_color(self, instance_chip, active_value: int):
            Animation(
                color=(0, 0, 0, 1) if active_value else (0, 0, 0, 0.5), d=0.2
            ).start(self.ids.label)
