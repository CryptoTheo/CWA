import importlib

from kivy.uix.popup import Popup
from kivymd.uix.textfield import MDTextField

import View.AboutUsScreen.about_us_screen

importlib.reload(View.AboutUsScreen.about_us_screen)


class AboutUsController:

    def __init__(self, model):
        self.model = model
        self.view = View.AboutUsScreen.about_us_screen.AboutUsScreen(
            controller=self, model=self.model
        )

    def get_view(self) -> View.AboutUsScreen.about_us_screen:
        return self.view

    # Menu Functions
    def search_button(self):
        print('search')

    def user_icon(self):
        # TODO make login popup
        popup = Popup(
            title='Admin Login',
            size_hint=(.9, .3),
            content=MDTextField(
                pos_hint={'center_x': .5, 'center_y': .5},
                password=True,
                helper_text_mode='on_focus',
                hint_text="Enter Password:",
                required=True,
                icon_left="key-variant",
                on_text_validate=lambda x: self.check_password(x),

            )
        )

        popup.open()
        print('user profile')

    def on_chevron_back(self):
        self.view.manager_screens.transition.direction = 'right'
        self.view.manager_screens.current = 'main screen'

    def check_password(self, x):
        if x.text == 'abc123':
            self.view.manager_screens.current = 'admin screen'

        else:
            self.view.manager_screens.current = 'main screen'
