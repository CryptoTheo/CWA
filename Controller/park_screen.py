import importlib

import View.ParkScreen.park_screen

importlib.reload(View.ParkScreen.park_screen)


class ParkScreenController:

    def __init__(self, model):
        self.model = model
        self.view = View.ParkScreen.park_screen.ParkScreenView(
            controller=self, model=self.model
        )

    def get_view(self) -> View.ParkScreen.park_screen:
        return self.view

    # Menu Functions
    def search_button(self):
        print('search')

    def user_icon(self):
        print('user profile')

    def on_chevron_back(self):
        self.view.manager_screens.transition.direction = 'right'
        self.view.manager_screens.current = 'main screen'
