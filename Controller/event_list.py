import importlib

import View.EventScreen.EventListScreen.event_list

importlib.reload(View.EventScreen.EventListScreen.event_list)


class EventListScreenController:

    def __init__(self, model):
        self.model = model
        self.view = View.EventScreen.EventListScreen.event_list.EventListScreenView(
            controller=self, model=self.model
        )

    def get_view(self) -> View.EventScreen.EventListScreen.event_list:
        return self.view

    # Menu Functions
    def search_button(self):
        print('search')

    def user_icon(self):
        print('user profile')

    def on_chevron_back(self):
        self.view.manager_screens.transition.direction = 'right'
        self.view.manager_screens.current = 'main screen'