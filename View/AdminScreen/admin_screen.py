from kivymd.uix.tab import MDTabs

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
