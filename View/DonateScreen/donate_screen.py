from View.MainScreen.components.Card.card import NavCard  # NOQA
from View.base_screen import BaseScreenView


class DonateScreenView(BaseScreenView):
    page_name = 'Donate'

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
