import json

from kivy.metrics import dp

from kivy.properties import StringProperty, ListProperty
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import MDList
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.tab import MDTabs, MDTabsBase

from View.EventScreen.EventListScreen.components.Results.results import ResultCard  # NOQA
from View.RiderScreen.components import RiderThumb
from View.base_screen import BaseScreenView
from database import Contest, ScoreCards, Rider


class Results(MDTabs):
    pass


class ResultList(MDList):
    pass


class Tab(MDFloatLayout, MDTabsBase):
    pass



class EventScreenView(BaseScreenView):
    page_name = StringProperty()
    contest_id = StringProperty()
    scorecards = ListProperty()
    current_rider_division = StringProperty()
    current_rider_name = StringProperty()
    current_trick_count = StringProperty(defaultvalue='0')
    current_overall = StringProperty(defaultvalue='0')
    current_kicker = StringProperty(defaultvalue='0')
    current_rail = StringProperty(defaultvalue='0')
    current_airtrick = StringProperty(defaultvalue='0')
    recent_overall = StringProperty(defaultvalue='0')
    recent_execution = StringProperty(defaultvalue='0')
    recent_creativity = StringProperty(defaultvalue='0')
    recent_difficulty = StringProperty(defaultvalue='0')
    recent_section = StringProperty(defaultvalue='Section')

    def on_enter(self, *args):
        contest = Contest.objects(id=self.app.active_contest).first()
        self.contest_id = str(contest.id)

        self.contest_format = contest.format

        self.scorecards = ScoreCards.objects(contest=self.contest_id, landed=True)
        if len(self.scorecards) <= 8:
            self.app.manager_screens.transition.direction = 'left'
            self.app.manager_screens.current = 'event list screen'
            Snackbar(text='No results yet!').open()
        else:
            self.page_name = contest.event_name
            self.generate_carasoul()
            self.generate_overall_ranking(str(contest.id))

    def generate_carasoul(self):
        riders = Rider.objects(on_water=True)

        riders_list = []
        for rider in riders:
            self.ids.on_water.add_widget(RiderThumb(
                rider_id=str(rider.id)
            ))
            riders_list.append(str(rider.id))

    def current_rider(self, rider_id):
        rider = Rider.objects(id=rider_id).first()

        self.current_rider_name = rider.get_display_name()
        self.current_rider_division = rider.get_division(self.contest_id)
        tricks = rider.get_trick_count(self.contest_id)
        if tricks is not None:
            self.current_trick_count = f'Scores:\n{tricks}'

        overall = rider.get_overall_scores(self.contest_id)
        if overall is not None:
            self.current_overall = f'Overall:\n{str(round(overall[0], 1))}'
            self.current_kicker = f'Kickers:\n{str(round(overall[1], 1))}'
            self.current_rail = f'Rails:\n{str(round(overall[2], 1))}'
            self.current_airtrick = f'AirTricks:\n{str(round(overall[3], 1))}'

        recent = rider.get_recent_scores(self.contest_id)
        if recent is not None:
            self.recent_section = f'Most Recent {str(recent[4])}'
            self.recent_overall = f' Overall: \n{str(round(recent[0], 1))}'
            self.recent_execution = f'Execution:\n{str(round(recent[1], 1))}'
            self.recent_creativity = f'Creativity:\n{str(round(recent[2], 1))}'
            self.recent_difficulty = f'Difficulty:\n{str(round(recent[3], 1))}'

    def generate_overall_ranking(self, contest_id):
        riders = Rider.objects(registered_contest=self.contest_id).order_by('overall')

        n = 1
        if self.ids.overall_list.children:
            self.ids.overall_list.clear_widgets()
        if riders is not None:
            for rider in riders:
                if rider.div_score > 0:
                    self.ids.overall_list.add_widget(ResultCard(
                        place=str(n),
                        rider_name=rider.display_name,
                        score=str(round(rider.overall, 1)),
                        division=rider.division
                    ))
                    n += 1

    def generate_rail_ranking(self, contest_id):
        riders = Rider.objects(registered_contest=self.contest_id).order_by('overall_rails')
        n = 1
        if self.ids.rail_list.children:
            self.ids.rail_list.clear_widgets()
        if riders is not None:
            for rider in riders:
                if rider.rail_division > 0:
                    self.ids.rail_list.add_widget(ResultCard(
                        place=str(n),
                        rider_name=rider.display_name,
                        score=str(round(rider.overall_rails, 1)),
                        division=rider.rail_div_label
                    ))

                n += 1

    def generate_airtrick_ranking(self, contest_id):
        riders = Rider.objects(registered_contest=self.contest_id).order_by('overall_airtricks')

        n = 1
        if self.ids.airtrick_list.children:
            self.ids.airtrick_list.clear_widgets()
        if riders is not None:
            for rider in riders:
                if rider.airtrick_division > 0:
                    self.ids.airtrick_list.add_widget(ResultCard(
                        place=str(n),
                        rider_name=rider.display_name,
                        score=str(round(rider.overall_airtricks, 1)),
                        division=rider.airtrick_div_label
                    ))

                    n += 1

    def generate_kicker_ranking(self, contest_id):
        riders = Rider.objects(registered_contest=self.contest_id).order_by('overall_kicker')

        n = 1
        if self.ids.kicker_list.children:
            self.ids.kicker_list.clear_widgets()
        if riders is not None:
            for rider in riders:
                if rider.kicker_division > 0:
                    self.ids.kicker_list.add_widget(ResultCard(
                        place=str(n),
                        rider_name=rider.display_name,
                        score=str(round(rider.overall_kickers, 1)),
                        division=str(rider.kicker_div_label)
                    ))

                    n += 1

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text) -> None:
        self.scorecards = ScoreCards.objects(contest=self.app.active_contest, landed=True)
        if tab_text == 'Overall':
            self.generate_overall_ranking(self.contest_id)

        if tab_text == 'Kickers':
            self.generate_kicker_ranking(self.contest_id)

        if tab_text == 'Rails':
            self.generate_rail_ranking(self.contest_id)

        if tab_text == 'AirTricks':
            self.generate_airtrick_ranking(self.contest_id)
