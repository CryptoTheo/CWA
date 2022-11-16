from kivymd.uix.tab import MDTabs

from View.AdminScreen.components.Create.Contests.create_contest import ContestsAdmin
from View.AdminScreen.components.Create.create import CreateTab
from View.AdminScreen.components.Judge.judge import JudgeTab
from View.AdminScreen.components.Manage.manage import ManageTab
from View.AdminScreen.components.Register.register_riders import RegisterRiders
from View.base_screen import BaseScreenView


class AdminTabBar(MDTabs):
    pass


class AdminScreenView(BaseScreenView):
    page_name = 'Admin'

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
