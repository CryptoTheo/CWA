from kivy.properties import ObjectProperty, StringProperty, ColorProperty, NumericProperty
from kivy.uix.popup import Popup
from kivymd.uix.card import MDCard
from kivymd.uix.snackbar import Snackbar

from View.AdminScreen.components.Judge.ScoreSheet.components.ScoreSlider.scoreslider import ScoreSlider
from database import ScoreCards, Rider


class ScoreCard(MDCard):
    image = ObjectProperty()
    rider_name = StringProperty()
    # rider_age = StringProperty()
    rider_stance = StringProperty()
    bib_color = ColorProperty()
    slider_value = NumericProperty()
    contest_id = StringProperty()
    rider_id = StringProperty()
    division = NumericProperty()
    execution = NumericProperty()
    creativity = NumericProperty()
    difficulty = NumericProperty()

    def submit_scores(self):
        # TODO Save scores to database
        if self.ids.kicker.active:
            section = 'Kicker'
        elif self.ids.rail.active:
            section = 'Rail'
        elif self.ids.air.active:
            section = 'Air Trick'
        else:
            Snackbar(text='ERROR: Select a Section!').open()
            return

        scorecard = ScoreCards()
        scorecard.contest = self.contest_id
        scorecard.rider_id = self.rider_id
        scorecard.display_name = self.rider_name
        scorecard.section = section
        scorecard.division = self.ids.division.slider_value
        scorecard.execution = self.ids.execution.slider_value
        scorecard.creativity = self.ids.creativity.slider_value
        scorecard.difficulty = self.ids.difficulty.slider_value
        scorecard.calc_average()
        scorecard.landed = True
        scorecard.save()

        self.clearcard('landed')

        # TODO Make scorecard go away onsubmit

    def rider_fell(self):
        if self.ids.kicker.active:
            section = 'Kicker'
        elif self.ids.rail.active:
            section = 'Rail'
        elif self.ids.air.active:
            section = 'Air Trick'
        else:
            Snackbar(text='ERROR: Select a Section!', md_bg_color=(1, 0, 0, 1)).open()
            return

        scorecard = ScoreCards()
        scorecard.contest = self.contest_id
        scorecard.rider_id = self.rider_id
        scorecard.display_name = self.rider_name
        scorecard.section = section
        scorecard.division = self.ids.division.slider_value
        scorecard.execution = 0
        scorecard.creativity = self.ids.creativity.slider_value
        scorecard.difficulty = self.ids.difficulty.slider_value
        scorecard.landed = False
        scorecard.save()

        self.clearcard('fell')
        # TODO Make scorecard go away onsubmit

    def clearcard(self, type):

        self.ids.division.slider_value = 0
        self.ids.execution.slider_value = 50
        self.ids.creativity.slider_value = 50
        self.ids.difficulty.slider_value = 50
        if type == 'fell':
            fall = Rider.objects(id=self.rider_id).get()
            fall.on_water = False
            fall.save()

        Snackbar(text='Submitted').open()

    # def dismiss(self, *_args, **kwargs):
    #     """ Close the view if it is open.
    #
    #     If you really want to close the view, whatever the on_dismiss
    #     event returns, you can use the *force* keyword argument::
    #
    #         view = ModalView()
    #         view.dismiss(force=True)
    #
    #     When the view is dismissed, it will be faded out before being
    #     removed from the parent. If you don't want this animation, use::
    #
    #         view.dismiss(animation=False)
    #
    #     """
    #     if not self._is_open:
    #         return
    #     self.dispatch('on_pre_dismiss')
    #     if self.dispatch('on_dismiss') is True:
    #         if kwargs.get('force', False) is not True:
    #             return
    #     if kwargs.get('animation', True):
    #         Animation(_anim_alpha=0., d=self._anim_duration).start(self)
    #     else:
    #         self._anim_alpha = 0
    #         self._real_remove_widget()
