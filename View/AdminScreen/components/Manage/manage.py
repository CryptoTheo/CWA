from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tab import MDTabsBase

from View.AdminScreen.components.Register.register_riders import SelectContest
from View.AdminScreen.components.tools.components import ListItemWithCheckbox
from database import Contest, Rider


class ManageTab(MDTabsBase, MDFloatLayout):
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
            ver_growth='down',
            max_height='120dp'
        )
        self.menu.open()
        print('menu')

    def callback(self, contest):
        self.ids.menu_.text = contest.event_name
        self.ids.menu_.hint_text = 'Editing:'
        self.menu.dismiss()
        self.update_list(contest)

    def update_list(self, contest):

        riders = Rider.objects()
        if self.ids.list.children:
            self.ids.list.clear_widgets()
        contest = Contest.objects(live=True).first()

        riders = Rider.objects(registered_contest=str(contest.id))
        if not riders:
            return
        else:
            for rider in riders:
                self.ids.list.add_widget(
                    ListItemWithCheckbox(
                        contest_id=str(contest.id),
                        rider_name=f'{rider.first_name} {rider.last_name}',
                        rider_id=str(rider.id),
                        active_check=rider.on_water,
                        bib_color=rider.bib_color,
                        type='on water'
                    )
                )
