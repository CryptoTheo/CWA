# from View.EventScreen.EventListScreen.components import EventCard  # NOQA
import mongoengine

from View.EventScreen.EventListScreen.components.EventCard.card import EventCard
from View.base_screen import BaseScreenView
from database import Contest


# TODO Redesign EventCard


class EventListScreenView(BaseScreenView):
    page_name = 'Events'

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_enter(self):

        if not self.ids.events_scroll.children:
            for contest in (Contest.objects()):
                self.ids.events_scroll.add_widget(EventCard(
                    event_name=contest.event_name,
                    event_description=contest.description,
                    event_format=contest.format,
                    event_date=contest.date,
                    event_location=contest.location,
                    # event_image=contest.image_link,
                    event_uid=str(contest.id)
                )
                )
