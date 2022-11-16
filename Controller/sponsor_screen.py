import importlib

import View.SponsorScreen.sponsor_screen

importlib.reload(View.SponsorScreen.sponsor_screen)


class SponsorScreenController:

    def __init__(self, model):
        self.model = model
        self.view = View.SponsorScreen.sponsor_screen.SponsorScreenView(
            controller=self, model=self.model
        )

    def get_view(self) -> View.SponsorScreen.sponsor_screen:
        return self.view

    # Menu Functions
    def search_button(self):
        print('search')

    def user_icon(self):
        print('user profile')

    def on_chevron_back(self):
        self.view.manager_screens.transition.direction = 'right'
        self.view.manager_screens.current = 'main screen'
