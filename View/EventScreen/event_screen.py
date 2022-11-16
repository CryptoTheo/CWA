import json

import pandas as pd
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


class ResultsTable(MDDataTable):
    column = ListProperty()
    row = ListProperty()


class EventScreenView(BaseScreenView):
    page_name = StringProperty()
    contest_id = StringProperty()
    scorecards = ListProperty()
    contest_format = StringProperty()
    average_division = StringProperty()
    average_creativity = StringProperty()
    average_execution = StringProperty()
    average_difficulty = StringProperty()
    average_score = StringProperty()
    latest_trick = StringProperty()
    percent_landed = StringProperty()
    rider_name = StringProperty()
    latest_creativity = StringProperty()
    latest_division = StringProperty()
    latest_execution = StringProperty()
    latest_difficulty = StringProperty()
    latest_section = StringProperty()

    def on_enter(self, *args):
        contest = Contest.objects(id=self.app.active_contest).first()
        self.contest_format = contest.format
        self.scorecards = ScoreCards.objects(contest=self.app.active_contest)
        if len(self.scorecards) <= 8:
            self.app.manager_screens.transition.direction = 'left'
            self.app.manager_screens.current = 'event list screen'
            Snackbar(text='No results yet!').open()
        else:
            self.contest_id = self.app.active_contest
            self.page_name = contest.event_name
            self.generate_overall()
            self.generate_carasoul()

    def generate_carasoul(self):
        rider = Rider.objects(on_water=True).to_json()
        rider = pd.DataFrame(pd.json_normalize(json.loads(rider)))

        for rider, score in rider.iterrows():
            self.ids.on_water.add_widget(RiderThumb(
                rider_id=score['_id.$oid'],
            ))

    def current_slide(self, rider_id):
        print(rider_id)
        rider = Rider.objects(id=rider_id).first()
        rider_name = f'{rider.first_name[0]}. {rider.last_name}'
        cards = ScoreCards.objects(contest=self.contest_id, rider_id=rider_id).to_json()
        cards = pd.DataFrame(pd.json_normalize(json.loads(cards)))
        averages = cards.groupby(['display_name']).mean(numeric_only=True)
        div = averages['division'][0]

        if 0.0 <= div < 20.0:
            div_label = 'Beginner'
        if 20.0 <= div < 40.0:
            div_label = 'Novice'
        if 40 <= div < 60:
            div_label = 'Intermediate'
        if 60 <= div < 90:
            div_label = 'Advanced'
        if div >= 90:
            div_label = 'Pro'

        self.rider_name = rider_name
        self.average_division = div_label
        self.average_creativity = str(averages["creativity"][0].round(1))
        self.average_execution = str(averages["execution"][0].round(1))
        self.average_difficulty = str(averages['difficulty'][0].round(1))
        self.average_score = str(averages['average'][0].round(1))

        latest_trick = cards.iloc[-1:]
        self.latest_creativity = str(latest_trick['creativity'].iloc[0].round(1))
        self.latest_division = str(latest_trick['average'].iloc[0].round(1))
        self.latest_execution = str(latest_trick['execution'].iloc[0].round(1))
        self.latest_difficulty = str(latest_trick['difficulty'].iloc[0].round(1))
        self.latest_section = str(latest_trick['section'].iloc[0].upper())
        print(self.latest_section)
        percent = averages['landed'].iloc[0]
        percent = percent * 10
        self.percent_landed = f"Landed: {str(percent)}%"

        print('end')
        # TODO the above is working!!! keep going!!! you got this!

    def generate_kickers(self):
        if self.ids.kicker_list.children:
            self.ids.kicker_list.clear_widgets()
        print('fresh data')
        cards = ScoreCards.objects(contest=self.app.active_contest).to_json()
        cards = pd.DataFrame(pd.json_normalize(json.loads(cards)))

        kickers = cards[cards['section'] == 'Kicker']
        results = kickers.groupby(['display_name']).mean(numeric_only=True)
        results = results.sort_values(['average'], ascending=False)

        n = 1
        scores = (ResultList(id='overall', spacing='12dp'))
        for rider, score in results.iterrows():
            div = score['division']
            if 0.0 <= div < 20.0:
                div_label = 'Beginner'
            if 20.0 <= div < 40.0:
                div_label = 'Novice'
            if 40 <= div < 60:
                div_label = 'Intermediate'
            if 60 <= div < 90:
                div_label = 'Advanced'
            if div >= 90:
                div_label = 'Pro'
            s = score['average'].round(1)
            creat = score['creativity'].round(1)
            ex = score['execution'].round(1)
            diff = score['difficulty'].round(1)

            s = s.round(1)

            item = ResultCard(
                place=str(n),
                rider_name=str(rider),
                score=str(s),
                creative=str(creat),
                execution=str(ex),
                difficulty=str(diff),
                division=div_label,
            )

            n += 1

            scores.add_widget(item)

        self.ids.kicker_list.add_widget(scores)

    def generate_rails(self):
        if self.ids.rail_list.children:
            self.ids.rail_list.clear_widgets()
        print('fresh data')
        cards = ScoreCards.objects(contest=self.app.active_contest).to_json()
        cards = pd.DataFrame(pd.json_normalize(json.loads(cards)))

        rails = cards[cards['section'] == 'Rail']
        results = rails.groupby(['display_name']).mean(numeric_only=True)
        results = results.sort_values(['average'], ascending=False)
        scores = (ResultList(id='overall', spacing='12dp'))
        n = 1

        for rider, score in results.iterrows():
            div = score['division']
            if 0.0 <= div < 20.0:
                div_label = 'Beginner'
            if 20.0 <= div < 40.0:
                div_label = 'Novice'
            if 40 <= div < 60:
                div_label = 'Intermediate'
            if 60 <= div < 90:
                div_label = 'Advanced'
            if div >= 90:
                div_label = 'Pro'
            s = score['average'].round(1)
            creat = score['creativity'].round(1)
            ex = score['execution'].round(1)
            diff = score['difficulty'].round(1)

            s = s.round(1)

            item = ResultCard(
                place=str(n),
                rider_name=str(rider),
                score=str(s),
                creative=str(creat),
                execution=str(ex),
                difficulty=str(diff),
                division=div_label,
            )

            n += 1

            scores.add_widget(item)

        self.ids.rail_list.add_widget(scores)

    def generate_airtricks(self):
        if self.ids.airtrick_list.children:
            self.ids.airtrick_list.clear_widgets()
        print('fresh data')
        cards = ScoreCards.objects(contest=self.app.active_contest).to_json()
        cards = pd.DataFrame(pd.json_normalize(json.loads(cards)))

        rails = cards[cards['section'] == 'Air Trick']
        results = rails.groupby(['display_name']).mean(numeric_only=True)
        results = results.sort_values(['average'], ascending=False)

        scores = (ResultList(id='overall', spacing='12dp'))
        n = 1

        for rider, score in results.iterrows():
            div = score['division']
            if 0.0 <= div < 20.0:
                div_label = 'Beginner'
            if 20.0 <= div < 40.0:
                div_label = 'Novice'
            if 40 <= div < 60:
                div_label = 'Intermediate'
            if 60 <= div < 90:
                div_label = 'Advanced'
            if div >= 90:
                div_label = 'Pro'
            s = score['average'].round(1)
            creat = score['creativity'].round(1)
            ex = score['execution'].round(1)
            diff = score['difficulty'].round(1)

            s = s.round(1)

            item = ResultCard(
                place=str(n),
                rider_name=str(rider),
                score=str(s),
                creative=str(creat),
                execution=str(ex),
                difficulty=str(diff),
                division=div_label,
            )

            n += 1
            scores.add_widget(item)

        self.ids.airtrick_list.add_widget(scores)

    def generate_overall(self):
        if self.ids.overall_list.children:
            self.ids.overall_list.clear_widgets()

        print('fresh data')
        cards = ScoreCards.objects(contest=self.app.active_contest).to_json()
        cards = pd.DataFrame(pd.json_normalize(json.loads(cards)))

        results = cards.groupby(['display_name']).mean(numeric_only=True)
        results = results.sort_values('average', ascending=False)
        results = results.sort_values(['average'], ascending=False)
        scores = (ResultList(id='overall', spacing='12dp'))
        n = 1

        for rider, score in results.iterrows():
            div = score['division']
            if 0.0 <= div < 20.0:
                div_label = 'Beginner'
            if 20.0 <= div < 40.0:
                div_label = 'Novice'
            if 40 <= div < 60:
                div_label = 'Intermediate'
            if 60 <= div < 90:
                div_label = 'Advanced'
            if div >= 90:
                div_label = 'Pro'
            s = score['average'].round(1)
            creat = score['creativity'].round(1)
            ex = score['execution'].round(1)
            diff = score['difficulty'].round(1)

            s = s.round(1)

            item = ResultCard(
                place=str(n),
                rider_name=str(rider),
                score=str(s),
                creative=str(creat),
                execution=str(ex),
                difficulty=str(diff),
                division=div_label,
            )

            n += 1

            scores.add_widget(item)
        self.ids.overall_list.add_widget(scores)

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text) -> None:
        self.scorecards = ScoreCards.objects(contest=self.app.active_contest)
        if tab_text == 'Overall':
            self.generate_overall()

        if tab_text == 'Kickers':
            self.generate_kickers()

        if tab_text == 'Rails':
            self.generate_rails()

        if tab_text == 'AirTricks':
            self.generate_airtricks()
