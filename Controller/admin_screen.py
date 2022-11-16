import importlib

import View.AdminScreen.admin_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.

importlib.reload(View.AdminScreen.admin_screen)


class AdminScreenController:
    """
    The `AdminScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.ScoreSheetModel
        self.view = View.AdminScreen.admin_screen.AdminScreenView(controller=self, model=self.model)

    def get_view(self) -> View.AdminScreen.admin_screen:
        return self.view

    # Menu Functions
    def search_button(self):
        print('search')

    def user_icon(self):
        print('user profile')

    def on_chevron_back(self):
        self.view.manager_screens.transition.direction = 'right'
        self.view.manager_screens.current = 'main screen'

    # def scorecard(self, rider):
    #     ScoreSheet.open_scorecard(rider)
