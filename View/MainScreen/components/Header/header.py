from kivy.properties import StringProperty
from kivymd.uix.toolbar import MDTopAppBar


class HeaderBar(MDTopAppBar):
    page_name = StringProperty()
