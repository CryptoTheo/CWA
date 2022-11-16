# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.
from Controller.about_us import AboutUsController
from Controller.admin_screen import AdminScreenController
from Controller.donate import DonateController
from Controller.event_list import EventListScreenController
from Controller.event_screen import EventScreenController
from Controller.main_screen import MainScreenController
from Controller.park_screen import ParkScreenController
from Controller.riders_screen import RidersScreenController
from Controller.sponsor_screen import SponsorScreenController
from Model.about_us import AboutUsModel
from Model.admin_screen import AdminScreenModel
from Model.donate import DonateModel
from Model.event import EventScreenModel
from Model.event_list import EventListModel
from Model.main_screen import MainScreenModel
from Model.park_screen import ParkScreenModel
from Model.riders_screen import RidersScreenModel
from Model.sponsor_screen import SponsorScreenModel

screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
    "event list screen": {
        "model": EventListModel,
        "controller": EventListScreenController,
    },
    "event screen": {
        "model": EventScreenModel,
        "controller": EventScreenController,
    },
    "rider screen": {
        "model": RidersScreenModel,
        "controller": RidersScreenController,
    },
    "admin screen": {
        "model": AdminScreenModel,
        "controller": AdminScreenController,
    },
    'park screen': {
        'model': ParkScreenModel,
        'controller': ParkScreenController,
    },
    'sponsor screen': {
        'model': SponsorScreenModel,
        'controller': SponsorScreenController
    },
    'about us': {
        'model': AboutUsModel,
        'controller': AboutUsController
    },
    'donate': {
        'model': DonateModel,
        'controller': DonateController
    }
}
