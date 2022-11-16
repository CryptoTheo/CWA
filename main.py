"""
Script for managing hot reloading of the project.
For more details see the documentation page -

https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/

To run the application in hot boot mode, execute the command in the console:
DEBUG=1 python main.py
"""
import certifi
import dns.resolver
import mongoengine as mongo
from kivy.uix.anchorlayout import AnchorLayout
# """
# The entry point to the application.
#
# The application uses the MVC template. Adhering to the principles of clean
# architecture means ensuring that your application is easy to test, maintain,
# and modernize.
#
# You can read more about this template at the links below:
#
# https://github.com/HeaTTheatR/LoginAppMVC
# https://en.wikipedia.org/wiki/Model–view–controller
# """
# #
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager

from View.screens import screens

# import importlib
# import os
#
# from kivy import Config
#
# import dns.resolver
#
# dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
# dns.resolver.default_resolver.nameservers = ['1.1.1.1']
#
# # TODO: You may know an easier way to get the size of a computer display.
# # Change the values of the application window size as you need.
# Config.set("graphics", "height", '600')
# Config.set("graphics", "width", "350")
#
# from kivy.core.window import Window
#
# # Place the application window on the right side of the computer screen.
# Window.top = 0
# Window.left = Window.width + 400
#
# import certifi
# import mongoengine as mongo
#
# try:
#     host_name = 'mongodb+srv://events.xfmhxnj.mongodb.net'
#     data = 'events'
#     username = 'admin'
#     password = 'nEXjgFKzF9yC2Z59'
#     mongo.connect(db=data,
#                   username=username,
#                   password=password,
#                   host=host_name,
#                   tlsCAFile=certifi.where())
# except Exception as e:
#     print(e)
#
# from kivymd.tools.hotreload.app import MDApp
# from kivymd.uix.screenmanager import MDScreenManager
# from kivymd.uix.transition import MDFadeSlideTransition
#
#
# class TheCWA(MDApp):
#     KV_DIRS = [os.path.join(os.getcwd(), "View")]
#     active_contest = ''
#     active_rider = ''
#     active_user = ''
#
#     def build_app(self) -> MDScreenManager:
#         """
#         In this method, you don't need to change anything other than the
#         application theme.
#         """
#
#         import View.screens
#         self.manager_screens = MDScreenManager(MDFadeSlideTransition())
#         Window.bind(on_key_down=self.on_keyboard_down)
#         importlib.reload(View.screens)
#         screens = View.screens.screens
#         self.theme_cls.theme_style = "Light"
#         self.theme_cls.primary_palette = "Blue"
#         self.theme_cls.primary_hue = "A200"
#
#         for i, name_screen in enumerate(screens.keys()):
#             model = screens[name_screen]["model"]()
#             controller = screens[name_screen]["controller"](model)
#             view = controller.get_view()
#             view.manager_screens = self.manager_screens
#             view.name = name_screen
#             self.manager_screens.add_widget(view)
#
#         return self.manager_screens
#
#     def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
#         """
#         The method handles keyboard events.
#
#         By default, a forced restart of an application is tied to the
#         `CTRL+R` key on Windows OS and `COMMAND+R` on Mac OS.
#         """
#
#         if "meta" in modifiers or "ctrl" in modifiers and text == "r":
#             self.rebuild()
#
#
# TheCWA().run()
# After you finish the project, remove the above code and uncomment the below
# code to test the application normally without hot reloading.

# TODO: You may know an easier way to get the size of a computer display.
# Change the values of the application window size as you need.

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['1.1.1.1']

try:
    host_name = 'mongodb+srv://events.xfmhxnj.mongodb.net'
    data = 'events'
    username = 'admin'
    password = 'nEXjgFKzF9yC2Z59'
    mongo.connect(db=data,
                  username=username,
                  password=password,
                  host=host_name,
                  tlsCAFile=certifi.where())
    connection = True
except Exception as e:
    print(e)
    connection = False


    class Example(MDApp):

        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Red"

            layout = AnchorLayout()
            self.card = MDCard(
                size_hint=(0.7, 0.6),
                md_bg_color=self.theme_cls.bg_dark,
                orientation='vertical'
            )
            label = MDLabel(
                text='Please connect to the internet and restart application',
                halign='center'
            )
            # error = MDLabel(
            #     text=e
            # )

            self.card.add_widget(label)
            # self.card.add_widget(error)
            layout.add_widget(self.card)

            return layout


class TheCWA(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = MDScreenManager()

    def build(self) -> MDScreenManager:
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self) -> None:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)


if __name__ == '__main__':
    if connection == True:
        TheCWA().run()
    else:
        Example().run()
