from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, ColorProperty, NumericProperty
from kivymd.uix.card import MDCard
from kivymd.uix.slider import MDSlider


def get_display(label, value):
    return f'{label}: {value}'


class ScoreSlider(MDCard):
    label = StringProperty()
    div = BooleanProperty()
    bib_color = ColorProperty()
    slider_value = NumericProperty(defaultvalue=50)

    def move_slider(self, *args):
        value = float(round(args[1], 2))
        self.slider_value = value
        if self.div == True:
            if value == 0:
                self.ids.score_value.text = 'First Timer'
            if 0.0 < value < 25.0:
                self.ids.score_value.text = 'Beginner'
            if 25.0 <= value < 50.0:
                self.ids.score_value.text = 'Novice'
            if 50 <= value < 75:
                self.ids.score_value.text = 'Intermediate'
            if 75 <= value < 100:
                self.ids.score_value.text = 'Advance'
            if value == 100:
                self.ids.score_value.text = 'Pro'
        else:
            display = get_display(self.label, value)
            self.ids.score_value.text = display

        return self.slider_value

