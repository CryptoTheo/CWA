from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.tab import MDTabsBase

from View.AdminScreen.components.tools.components import ListItemWithCheckbox
from database import Rider, Contest


class SelectContest(FloatLayout):
    pass

class RegisterRiders(MDRelativeLayout, MDTabsBase):
    header_text = StringProperty()

    def start_search(self):
        for contest in Contest.objects():
            self.menu_list = [
                {
                    "viewclass": "OneLineListItem",
                    "text": contest.event_name,
                    "on_release": lambda x=contest: self.callback(x)
                }
            ]
        self.menu = MDDropdownMenu(
            caller=self.ids.menu_,
            items=self.menu_list,
            width_mult=4,
            ver_growth='down'
        )
        self.menu.open()
        print('menu')

    def callback(self, contest):
        if contest == '':
            return
        self.ids.menu_.text = contest.event_name
        self.ids.menu_.hint_text = 'Editing:'
        self.menu.dismiss()
        self.update_list(contest)

    def update_list(self, contest):

        if self.ids.list.children:
            self.ids.list.clear_widgets()

        riders = Rider.objects()
        for rider in riders:
            if str(contest.id) in rider.registered_contest:
                registerd = True
            else:
                registerd = False
            self.ids.list.add_widget(
                ListItemWithCheckbox(
                    contest_id=str(contest.id),
                    rider_name=f'{rider.first_name} {rider.last_name}',
                    rider_id=str(rider.id),
                    active_check=registerd,
                    bib_color=rider.bib_color,
                    type='register'
                )
            )
