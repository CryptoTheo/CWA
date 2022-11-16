from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

from View.AdminScreen.components.Judge.ScoreSheet.components.RiderThumb.riders_thumb import RidersThumb
from View.AdminScreen.components.Judge.ScoreSheet.components.ScoreCard.scorecard import ScoreCard
from database import Contest, Rider


class MyCheckBar(MDCard):
    pass

class ScoreSheet(MDCard):

    def on_enter(self):
        contest = Contest.objects(live=True).first()
        riders = Rider.objects(on_water=True)

        if not self.ids.water.children:
            for rider in riders:
                self.ids.water.add_widget(RidersThumb(
                    id=str(rider.id),
                    rider_name=f'{rider.first_name[0]}. {rider.last_name}',
                    rider_id=str(rider.id),
                    contest_id=str(contest.id),
                    rider_stance=rider.stance,
                    bib_color=rider.bib_color,
                    on_press=lambda x: self.open_scorecard(x)
                ))

    def open_scorecard(self, rider):
        contest = Contest.objects(live=True).first()
        riders = Rider.objects(on_water=True)
        if self.ids.water.children:
            self.ids.water.clear_widgets()
            for card in riders:
                rid = str(card.id)
                self.ids.water.add_widget(RidersThumb(
                    id=str(card.id),
                    rider_name=f'{card.first_name[0]}. {card.last_name}',
                    rider_id=str(card.id),
                    contest_id=str(contest.id),
                    rider_stance=card.stance,
                    bib_color=card.bib_color,
                    on_press=lambda x=rid: self.open_scorecard(x)
                ))
        if self.ids.scorecard.children:
            self.ids.scorecard.clear_widgets()

        self.ids.scorecard.add_widget(ScoreCard(
            bib_color=rider.bib_color,
            rider_name=rider.rider_name,
            rider_id=rider.rider_id,
            contest_id=str(contest.id),
            rider_stance=rider.rider_stance,

        ))


class JudgeTab(MDTabsBase, MDFloatLayout):
    # def __init__(self, **kwargs):
    #     super(JudgeTab, self).__init__(**kwargs)
    #
    #     box = MDBoxLayout()
    #     if not self.children:
    #         for rider in riders:
    #             rid = str(rider.id)
    #             print(rid)
    #             btn = RidersThumb(
    #                 id=str(rider.id),
    #                 rider_name=f'{rider.first_name[0]}. {rider.last_name}',
    #                 rider_id=str(rider.id),
    #                 on_press=lambda x=rid: self.open_scorecard(rid))
    #
    #             box.add_widget(btn)
    #
    #
    #
    #         self.add_widget(box)
    #
    # def open_scorecard(self, x):
    #     rider = Rider.objects(id=x).get()
    #     print(rider.first_name)
    pass