
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.tab import MDTabsBase

from database import Rider, Contest


class ContestsAdmin(MDCard):
    filename = StringProperty()
    url = StringProperty()

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_time_save, on_cancel=self.on_cancel)
        time_dialog.open()

    def on_date_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''

        self.ids.date.text = str(value)
        # print(instance, value, date_range)
        # print((value))

    def on_time_save(self, instance, value):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''

        self.ids.time.text = str(value)
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

    def add_contest(self):
        # TODO Add error protection

        contest = Contest()
        contest.event_name = self.ids.event_name.text
        contest.location = self.ids.location.text
        contest.description = self.ids.description.text
        contest.image_link = self.ids.image_link.text
        contest.format = self.ids.format.text
        contest.date = self.ids.date.text
        contest.start_time = self.ids.time.text
        contest.save()
        self.clear_form()
        Snackbar(text='Contest Added Successfully').open()

    def clear_form(self):
        self.ids.event_name.text = ''
        self.ids.location.text = ''
        self.ids.description.text = ''
        self.ids.image_link.text = ''
        self.ids.format.text = ''
        self.ids.date.text = 'Event Date'
        self.ids.time.text = 'Start Time'
