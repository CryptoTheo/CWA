from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.list import OneLineListItem, OneLineAvatarIconListItem, IRightBodyTouch, MDList, \
    TwoLineAvatarIconListItem, BaseListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.toolbar import MDTopAppBar

from View.AdminScreen.components.tools.components import ListItemWithCheckbox
from database import Rider, Contest


class DockHand(MDCard):
    header_text = StringProperty()
