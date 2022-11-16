import importlib

import View.DonateScreen.donate_screen

importlib.reload(View.DonateScreen.donate_screen)


class DonateController:

    def __init__(self, model):
        self.model = model
        self.view = View.DonateScreen.donate_screen.DonateScreenView(
            controller=self, model=self.model
        )

    def get_view(self) -> View.DonateScreen.donate_screen:
        return self.view

    # Menu Functions
    def search_button(self):
        print('search')

    def user_icon(self):
        print('user profile')

    def on_chevron_back(self):
        self.view.manager_screens.transition.direction = 'right'
        self.view.manager_screens.current = 'main screen'
