from View.RiderScreen.components import RiderThumb  # NOQA
from View.base_screen import BaseScreenView


# Todo Start Over

class AboutUsScreen(BaseScreenView):
    page_name = 'About Us'
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
