from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.card import MDCard
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.snackbar import Snackbar

from database import Rider


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


class ListItemWithCheckbox(MDCard):
    '''Custom list item.'''
    rider_name = StringProperty()
    rider_id = StringProperty()
    active_check = BooleanProperty()
    contest_id = StringProperty()
    type = StringProperty()
    bib_color_text = StringProperty(defaultvalue='Pick a Color')
    bib_color = StringProperty()


    def on_checkbox_active(self, type):
        if type == 'on water':
            status = self.ids.check.active
            rider = Rider.objects(id=self.rider_id).get()

            if status:
                rider.on_water = True
                Snackbar(text='Rider is on the Cable!!!').open()

            if not status:
                rider.on_water = False
                Snackbar(text='Rider Fell').open()

            rider.save()

        if type == 'register':
            status = self.ids.check.active
            rider = Rider.objects(id=self.rider_id).get()

            # if status is active, register the rider to the contest
            if status:
                rider.registered_contest.append(self.contest_id)
                Snackbar(text='Rider Registered Successfully').open()

            # if status is inactive, remove rider from contest
            if not status:
                rider.update(pull__registered_contest=self.contest_id)
                Snackbar(text='Rider Removed Successfully').open()
            rider.save()
        return

    def select_bib_color(self):
        bib_colors = ['red', 'grey', 'blue', 'yellow', ]
        self.menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text": color,
                "on_release": lambda x=color: self.set_bib_color(x)
            } for color in bib_colors
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.colour,
            items=self.menu_list,
            width_mult=2,
            ver_growth='down'
        )
        self.menu.open()

    def set_bib_color(self, bib_color):
        self.ids.colour.md_bg_color = bib_color
        rider = Rider.objects(id=self.rider_id).get()
        rider.bib_color = bib_color
        print(rider.bib_color)
        rider.save()

        if bib_color == 'grey':
            bib_color = 'black'

        self.ids.color_label.text = bib_color.capitalize()
        self.menu.dismiss()

        print('callback')
        print(self)
        print(bib_color)

