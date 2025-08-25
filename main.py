from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class BaseScreen(Screen):
    def __init__(self, screen_manager, screen_name, **kwargs):
        super().__init__(name=screen_name, **kwargs)

        root = FloatLayout()

        root.add_widget(Label(
            text=f"Вы на экране: {screen_name}",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            font_size=24
        ))

        top_buttons_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(0.5, 0.1),  # половина ширины экрана, 10% высоты
            pos_hint={"center_x": 0.5, "top": 0.3},
            spacing=10
        )

        btn_top1 = Button(text="Доходы")
        btn_top2 = Button(text="Расходы")

        btn_top1.bind(on_press=lambda x: setattr(screen_manager, "current", "special"))
        btn_top2.bind(on_press=lambda x: setattr(screen_manager, "current", "special"))


        top_buttons_layout.add_widget(btn_top1)
        top_buttons_layout.add_widget(btn_top2)
        root.add_widget(top_buttons_layout)

        # Контейнер для кнопок снизу
        buttons_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(1, 0.15),       # ширина = 100%, высота = 15%
            pos_hint={"x": 0, "y": 0}, # прикрепляем снизу
            spacing=10,
            padding=10
        )

        # Четыре кнопки
        btn1 = Button(text="История")
        btn2 = Button(text="Статистика")
        btn3 = Button(text="Планнирование")
        btn4 = Button(text="Настройки")

        # Настраиваем перключение экранов
        btn1.bind(on_press=lambda x: setattr (screen_manager, "current", "history"))
        btn2.bind(on_press=lambda x: setattr(screen_manager, "current", "stats"))
        btn3.bind(on_press=lambda x: setattr(screen_manager, "current", "plan"))
        btn4.bind(on_press=lambda x: setattr(screen_manager, "current", "settings"))

        # Добавляем их в контейнер
        buttons_layout.add_widget(btn1)
        buttons_layout.add_widget(btn2)
        buttons_layout.add_widget(btn3)
        buttons_layout.add_widget(btn4)

        root.add_widget(buttons_layout)
        self.add_widget(root)

class SpecialScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(name="special", **kwargs)
        root = FloatLayout()

        root.add_widget(Label(
            text="Это новый экран!",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size=28
        ))

        self.add_widget(root)

class MainApp(App):
    def build(self):
        sm = ScreenManager()

        # Создаем экраны
        sm.add_widget(BaseScreen(sm, "history"))
        sm.add_widget(BaseScreen(sm, "stats"))
        sm.add_widget(BaseScreen(sm, "plan"))
        sm.add_widget(BaseScreen(sm, "settings"))
        sm.add_widget(SpecialScreen())

        return sm


if __name__ == "__main__":
    MainApp().run()




