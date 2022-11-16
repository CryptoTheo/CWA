import importlib

import View.RiderScreen.riders_screen

importlib.reload(View.RiderScreen.riders_screen)


class RidersScreenController:

    def __init__(self, model):
        self.model = model
        self.view = View.RiderScreen.riders_screen.RidersScreenView(
            controller=self, model=self.model
        )

    def get_view(self) -> View.RiderScreen.riders_screen:
        return self.view

    # Menu Functions
    def search_button(self):
        print('search')

    def user_icon(self):
        print('user profile')

    def on_chevron_back(self):
        self.view.manager_screens.transition.direction = 'right'
        self.view.manager_screens.current = 'main screen'
